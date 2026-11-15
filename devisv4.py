lines = [
    {
        "description" : "Dépose carrelage",
        "quantity" : 12,
        "unit" : "m2",
        "price_per_unit" : 25   },
    {
        "description" : "Pose de faïence",
        "quantity" : 12,
        "unit" : "m2",
        "price_per_unit" : 45   },
    {
        "description" : "Remplacement mitigeur",
        "quantity" : 1,
        "unit" : "u",
        "price_per_unit" : 120   },
    {
        "description" : "Joint silicone",
        "quantity" : 5,
        "unit" : "ml",
        "price_per_unit" : 8   },
    {
        "description" : "",
        "quantity" : 2,
        "unit" : "u",
        "price_per_unit" : 50   },
    {
        "description" : "Peinture plafond",
        "quantity" : 0,
        "unit" : "m2",
        "price_per_unit" : 20   },
    {
        "description" : "Plinthes",
        "quantity" : 10,
        "unit" : "metres",
        "price_per_unit" : 6   }  
]

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

print(line_total({"description": "Test", "quantity": 3, "unit": "u", "price_per_unit": 10}))
print(check_line({"description": "Test", "quantity": -1, "unit": "u", "price_per_unit": 10}, allowed_units))

print_quote(lines, allowed_units, 10)
