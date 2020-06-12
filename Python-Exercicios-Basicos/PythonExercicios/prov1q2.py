print("-=-" * 17)
print("Olá, seja muito Bem Vindo ao parque Ambrolândia!")
print("-=-" * 17)
idade = int(input("Qual sua idade? "))
altura = int(input("Qual sua altura? (em Cm)"))

# Conversão cm para m
alturacm = altura / 100
cont = 0

if (idade >= 12) and (alturacm >= 1.5):
    print("1 brinquedo: Barca Viking")
elif (idade >= 14) and (alturacm >= 1.4):
    print("2 briquedos: Barca Viking e Elevator of Death")
elif (idade >= 16) or (alturacm >= 1.7):
    print("3 brinquedos: Barca Viking, Elevator of Death e Final Killer.")
else:
    print("Você ainda não pode andar nos brinquedos")
