description = "Pose de faïence"
quantity = 12
unit_of_quantity = "m2"
price_per_unit = 45
excl_VAT = price_per_unit * quantity
rate = 10
VAT = excl_VAT * rate/100
incl_VAT = excl_VAT + VAT


print(f"{description}, {quantity} {unit_of_quantity}, à {price_per_unit:.2f} euros le {unit_of_quantity}")
print(f"prix HT : {excl_VAT:.2f}, TVA : {VAT:.2f}, TTC : {incl_VAT:.2f}")