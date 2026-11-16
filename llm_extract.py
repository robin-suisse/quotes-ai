import json
import ollama

SYSTEM_PROMPT = """
Tu aides un artisan à extraire les travaux réellement demandés dans une note de chantier.

Réponds uniquement avec un JSON valide, au format :
{"lines": [{"description": "...", "quantity": nombre, "unit": "..."}]}

Utilise uniquement ces unités : "m2", "ml", "u", "h", "forfait".
La quantité doit toujours être un nombre.
N’inclus aucun prix ni champ lié aux prix.
N’invente aucun travail, aucune quantité ni aucune unité absents de la note.

Si la note ne contient aucun travail demandé, réponds exactement :
{"lines": []}

Ignore les éléments précédés d’une négation ou d’une interdiction : ce ne sont pas des travaux à réaliser.
N’interprète pas une abréviation si son sens n’est pas clair. Ignore-la plutôt que de deviner ou d’inventer un travail.

Exemple :
Note : « Dans la cuisine, poser du carrelage sur 8 m2 et peindre les murs sur 20 m2. »
Réponse :
{"lines": [{"description": "Pose de carrelage", "quantity": 8, "unit": "m2"}, {"description": "Peinture des murs", "quantity": 20, "unit": "m2"}]}

Exemple sans travaux :
Note : « Le client veut que ce soit fini avant Noël. »
Réponse :
{"lines": []}
"""

test_notes = [
    "SDB 6m2 virer vieux carrelage + faience, changer mitigeur",
    "repeindre le salon",
    "chambre: peinture murs 12 m2, ne pas toucher au parquet",
    "client veut que ce soit fini avant Noël",
    "cuisine 8m2 poser carrelage, repeindre plafond 10m2",
    "ch. 10m2 repeindre murs, pdt ne pas toucher aux plinthes",
    "sdb refaire joints douche 4 ml, changer robinet lavabo",
    "salon 20m2 poncer parquet et vitrifier, enfin je crois 18m2",
]
for note in test_notes:

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": note},
        ],
        format="json",
        options={"temperature": 0},
    )

    raw_text = response["message"]["content"]
    print(raw_text)

    data = json.loads(raw_text)
    for line in data["lines"]:
        print(line["description"], line["quantity"], line["unit"])