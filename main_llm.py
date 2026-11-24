from llm_utils import extract_lines
from quotes_utils import allowed_units, print_quote
from catalog_utils import load_catalog, price_lines

note = "salle de bain 6 m2, enlever le vieux carrelage, poser de la faïence, changer le mitigeur"
catalog = load_catalog()

lines = extract_lines(note, catalog)

priced_lines, manual_lines = price_lines(lines, catalog)

print_quote(priced_lines, allowed_units, 10)
print("À chiffrer manuellement :")
for line in manual_lines:
    print("-", line["description"])