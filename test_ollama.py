import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": "Tu aides un artisan à relever les travaux mentionnés dans une note de chantier. Identifie chaque travail et réponds sous forme de liste à puces, avec un seul travail par ligne. N’ajoute aucun autre texte, titre ou commentaire."},
        {"role": "user", "content": "salle de bain 6 m2, enlever le vieux carrelage, poser de la faïence, changer le mitigeur"},
    ],
    options={"temperature": 0},
)

answer = response["message"]["content"]
print(answer)