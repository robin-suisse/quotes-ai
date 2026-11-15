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

total_excl_vat = 0
for number, line in enumerate(lines, start=1):
    if line["description"] == "":
        print(f"{number}. Ligne ignorée : description vide")
    elif line["quantity"] <= 0:
        print(f"{number}. Ligne ignorée : quantité invalide")
    elif line["unit"] not in allowed_units:
        print(f'{number}. Ligne ignorée : unité inconnue "{line["unit"]}"')
    else:
        line_total = line["quantity"] * line["price_per_unit"]
        print(f"{number}. {line["description"]} : {line_total:.2f} €")
        total_excl_vat += line_total

vat_rate = 20
vat = total_excl_vat * vat_rate/100
incl_vat = total_excl_vat + vat

print(f"Total HT: {total_excl_vat:.2f} €")
print(f"TVA ({vat_rate} %): {vat:.2f} €")
print(f"Total TTC: {incl_vat:.2f} €")

