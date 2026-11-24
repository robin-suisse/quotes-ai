import ollama
from models import ExtractedQuote
from pydantic import ValidationError
from catalog_utils import catalog_for_prompt

SYSTEM_PROMPT = """
Tu aides un artisan à extraire les travaux réellement demandés dans une note de chantier.

Réponds uniquement avec un JSON valide, au format :
{"lines": [{"code": "...", "description": "...", "quantity": nombre, "unit": "...", "price_per_unit": nombre ou null}]}

Utilise uniquement ces unités : "m2", "ml", "u", "h", "forfait" .
La quantité doit toujours être un nombre.
price_per_unit est le prix unitaire en euros, uniquement s'il est écrit dans la note. S'il n'est pas écrit, mets null. N'invente jamais un prix.
N’invente aucun travail, aucune quantité ni aucune unité absents de la note.
N'utilise un code du catalogue que si c'est exactement le même travail. Garde toujours la description, la quantité et l'unité telles que l'artisan les a écrites. Pour un nombre de pièces (planches, prises...), l'unité est "u".

Pour chaque travail, choisis le code le plus adapté dans le catalogue ci-dessous. Si aucun code ne correspond, utilise le code “AUTRE”. N’invente jamais de code.
Si un travail n'est pas dans le catalogue, utilise le code "AUTRE", mais extrais quand même sa description, sa quantité, son unité et son prix.

Si la note ne contient aucun travail demandé, réponds exactement :
{"lines": []}

Ignore les éléments précédés d’une négation ou d’une interdiction : ce ne sont pas des travaux à réaliser.
N’interprète pas une abréviation si son sens n’est pas clair. Ignore-la plutôt que de deviner ou d’inventer un travail.
N'ajoute jamais un travail du catalogue s'il n'est pas demandé dans la note, même s'il semble logique.

Exemple :
Note : « Dans la cuisine, poser du carrelage sur 8 m2 à 40 € le m2 et peindre les murs sur 20 m2. »
Réponse :
{"lines": [{"code": "POSE_CARRELAGE_SOL", "description": "Pose de carrelage", "quantity": 8, "unit": "m2", "price_per_unit": 40}, {"code": "PEINTURE_MURS", "description": "Peinture des murs", "quantity": 20, "unit": "m2", "price_per_unit": null}]}

Exemple sans travaux :
Note : « Le client veut que ce soit fini avant Noël. »
Réponse :
{"lines": []}
"""

MAX_ATTEMPTS = 3

def extract_lines(note, catalog):
    full_prompt = SYSTEM_PROMPT + "\nCatalogue des prestations :\n" + catalog_for_prompt(catalog)
    messages = [
        {"role": "system", "content": full_prompt},
        {"role": "user", "content": note},
    ]
    for attempt in range(1, MAX_ATTEMPTS + 1):  
        response = ollama.chat(
                model="llama3.2",
                messages=messages,
                format="json",
                options={"temperature": 0},
            )
        raw_text = response["message"]["content"]

        try:
            extracted_quote = ExtractedQuote.model_validate_json(raw_text)
            return extracted_quote.model_dump()["lines"]
        except ValidationError as error:
            messages.append({"role": "assistant", "content": raw_text})
            messages.append({"role": "user", 
                            "content": f"Ta réponse ne respecte pas le format : {error}. Corrige-la et renvoie uniquement le JSON."
                            })

    raise ValueError(f"Réponse invalide après {MAX_ATTEMPTS} essais")

    
    
