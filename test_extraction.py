from llm_utils import extract_lines

test_notes = [
    "SDB 6m2 virer vieux carrelage + faience, changer mitigeur",
    "repeindre le salon",
    "chambre: peinture murs 12 m2, ne pas toucher au parquet",
    "client veut que ce soit fini avant Noël",
    "cuisine 8m2 poser carrelage, repeindre plafond 10m2",
    "ch. 10m2 repeindre murs, pdt ne pas toucher aux plinthes",
    "sdb refaire joints douche 4 ml, changer robinet lavabo",
    "salon 20m2 poncer parquet et vitrifier, enfin je crois 18m2",
]

accepted = 0
refused = 0

for note in test_notes:
    print("NOTES : ", note)
    try:
        lines = extract_lines(note)
        print("OK : ", len(lines), 'ligne(s)')
        accepted+=1
    except ValueError as error:
        print("REFUSÉ : ", error)
        refused+=1
    print("")

print("ACCEPTED : ", accepted)
print("REFUSED : ", refused)

