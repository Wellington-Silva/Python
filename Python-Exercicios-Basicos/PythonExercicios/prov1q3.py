q_people = int(input("Quantidade de pessoas: "))
city = str(input("Cidade: "))
quan_quart = int(input("Quantidade de Quartos: "))

if (city == "Pipa"):
    if (quan_quart == 2):
        total = 600 + (q_people * 75)
        v_people = total / q_people
        print("Valor total: %.2f" % total)
        print("Valor por pessoa: %.2f" % v_people)
    else:
        total = 900 + (q_people * 75)
        v_people = total / q_people
        print("Valor total: %.2f " % total)
        print("Valor por pessoa: %.2f" % v_people)

elif (city == "Fortaleza"):
    if (quan_quart == 3):
        total = 950 + (q_people * 60)
        v_people = total / q_people
        print("Valor total: %.2f" % total)
        print("Valor por pessoa: %.2f" % v_people)
    else:
        total = 1120 + (q_people * 60)
        v_people = total / q_people
        print("Valor total: %.2f" % total)
        print("Valor por pessoa: %.2f" % v_people)