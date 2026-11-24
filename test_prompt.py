from catalog_utils import load_catalog
from llm_utils import extract_lines

catalog = load_catalog()
note = "salle de bain 6 m2, enlever le vieux carrelage, poser de la faïence, changer le mitigeur"
for line in extract_lines(note, catalog):
    print(line)