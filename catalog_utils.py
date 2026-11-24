import json

def load_catalog():
    with open("catalog.json", encoding="utf-8") as f:
        return json.load(f)

def price_lines(lines, catalog):
    found = []
    missing = []
    for line in lines:
        code = line["code"]
        if code in catalog:
            line["price_per_unit"] = catalog[code]["price"]
            found.append(line)
        else:
            missing.append(line)
    return found, missing

def catalog_for_prompt(catalog):
    text = ""
    for code in catalog:
        text += f"- {code} : {catalog[code]['label']} ({catalog[code]['unit']})\n"
    return text