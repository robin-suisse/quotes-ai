import json
from quotes_utils import print_quote, allowed_units

with open("lines.json", encoding="utf-8") as f:
    loaded_lines = json.load(f)

llm_text = '[{"description": "Pose parquet", "quantity": 20, "unit": "m2", "price_per_unit": 35}, {"description": "Plinthes", "quantity": 18, "unit": "ml", "price_per_unit": 7}]'
data_llm = json.loads(llm_text)

print_quote(data_llm, allowed_units, 10)
print_quote(loaded_lines, allowed_units, 10)
