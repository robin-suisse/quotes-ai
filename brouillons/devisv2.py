nb_lines = int(input("Combien de lignes ? "))
lines = []

for i in range (nb_lines):

    line = {
        "description" : input("Description : "),
        "quantity" : float(input("Quantité : ")), 
        "unit" : input("Unité : "), 
        "price_per_unit" : float(input("Prix par unité : "))}
    
    lines.append(line)

for line in (lines):
    print (
        "Description : ", line["description"],
        "Quantité : ", line["quantity"],
        "Unité : ", line["unit"],
        "Prix unitaire : ", line["price_per_unit"]
    )

print(lines[2]["description"])
print("Total HT ligne 2 : ", lines[1]["quantity"] * lines[1]["price_per_unit"])

line = {
        "description" : input("Description : "),
        "quantity" : float(input("Quantité : ")), 
        "unit" : input("Unité : "), 
        "price_per_unit" : float(input("Prix par unité : "))}

print(len(lines))
lines.append(line)
print(len(lines))
