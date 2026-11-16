import json

allowed_units = ["m2", "ml", "u", "h", "forfait"]

def line_total(line):
    return line["quantity"] * line["price_per_unit"]

def check_line(line, allowed_units):
    if line["description"] == "":
        return "description vide"
    elif line["quantity"] <= 0:
        return "quantité invalide"
    elif line["unit"] not in allowed_units:
        return f'unité inconnue "{line["unit"]}"'
    else:
        return ""

def print_quote(lines, allowed_units, vat_rate):
    total_excl_vat = 0

    for number, line in enumerate(lines, start=1):
        error = check_line(line, allowed_units)

        if error != "":
            print(f"{number}. Ligne ignorée : {error}")
            continue

        price = line_total(line)
        print(f"{number}. {line["description"]} : {price:.2f} €")
        total_excl_vat += price

    vat = total_excl_vat * vat_rate/100
    incl_vat = total_excl_vat + vat

    print(f"Total HT: {total_excl_vat:.2f} €")
    print(f"TVA ({vat_rate} %): {vat:.2f} €")
    print(f"Total TTC: {incl_vat:.2f} €")


#with open("lines.json", "w", encoding="utf-8") as f:
    #json.dump(lines, f, ensure_ascii=False, indent=2)
    
with open("lines.json", encoding="utf-8") as f:
    loaded_lines = json.load(f)

llm_text = '[{"description": "Pose parquet", "quantity": 20, "unit": "m2", "price_per_unit": 35}, {"description": "Plinthes", "quantity": 18, "unit": "ml", "price_per_unit": 7}]'
data_llm = json.loads(llm_text)

print(line_total({"description": "Test", "quantity": 3, "unit": "u", "price_per_unit": 10}))
print(check_line({"description": "Test", "quantity": -1, "unit": "u", "price_per_unit": 10}, allowed_units))

print_quote(data_llm, allowed_units, 10)
print_quote(loaded_lines, allowed_units, 10)
