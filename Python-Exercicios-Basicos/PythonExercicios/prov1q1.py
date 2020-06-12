media  = float(input("Qual a média? "))
n_aulas = int(input("Qual o nº de aulas? "))
n_faltas = int(input("Qual a quantidade de faltas?"))

frequencia = n_aulas - n_faltas
freq = (frequencia/100)*frequencia

if (media >= 5) and (freq >= 75):
    print("APROVADO")
elif (media >= 7) and (freq >= 50):
    print("APROVADO")
else:
    print("REPROVADO")