from llm_utils import extract_lines
from quotes_utils import allowed_units, print_quote
from catalog_utils import load_catalog

note = "salle de bain 6 m2, enlever le vieux carrelage, poser de la faïence, changer le mitigeur"
catalog = load_catalog()

lines = extract_lines(note, catalog)

for line in lines:
    line["price_per_unit"] = 50

print_quote(lines, allowed_units, 10)