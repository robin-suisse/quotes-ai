from catalog_utils import load_catalog, price_lines
from quotes_utils import allowed_units, print_quote

lines = [
    {"code": "DEPOSE_CARRELAGE", "description": "Dépose carrelage", "quantity": 6, "unit": "m2"},
    {"code": "REMPLACEMENT_MITIGEUR", "description": "Remplacement mitigeur", "quantity": 1, "unit": "u"},
    {"code": "POSE_VELUX", "description": "Pose d'un velux", "quantity": 1, "unit": "u"},
]

catalog = load_catalog()
priced_lines, manual_lines = price_lines(lines, catalog)

print_quote(priced_lines, allowed_units, 10)

print("À chiffrer manuellement :")
for line in manual_lines:
    print("-", line["description"])