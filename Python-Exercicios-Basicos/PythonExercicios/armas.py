nation = str(input("Qual sua Nacionalidade? "))
ocupa = str(input("Qual sua ocupação? "))
q_guns = int(input("COm quantas armas voçê está? "))
caliber = int(input("Qual o calibre? "))
ent = 0
if (nation == "B") and (ocupa == "M"):
    ent = ent + 1
if (nation == "B") and (ocupa == "T" or "O") and (q_guns == 1) and(caliber == 22):
    ent = ent + 1
if (nation == "B") and (ocupa == "C") and (q_guns == 2) and (caliber == 38):
    ent = ent + 1
if (nation == "E") and (q_guns == 0) and (caliber >= 0):
    ent = ent + 1
if (ent >= 1):
    print("Liberado")

else:
    print("Barrado")


