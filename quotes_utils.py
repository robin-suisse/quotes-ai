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

def quote_totals(lines, vat_rate):
    total_excl_vat = 0
    
    for line in lines:
        price = line_total(line)
        total_excl_vat += price
    
    vat = total_excl_vat * vat_rate/100
    incl_vat = total_excl_vat + vat
    return {"excl_vat": total_excl_vat, "vat": vat, "incl_vat": incl_vat}
