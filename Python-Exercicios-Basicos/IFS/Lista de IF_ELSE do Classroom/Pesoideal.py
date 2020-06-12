nome   = input("Nome: ")
sexo   = input("Sexo (M-Masculino e F-Feminino): ")
idade  = int(input("Idade: "))
altura = float(input("Altura: "))
pesoIdeal = 0

#considerando que o Sexo é M-Masculino e F-Feminino
if (sexo == "M"):
  if (altura > 1.7):
    if (idade <= 20):
      pesoIdeal = (72.7*altura) - 58
    else:
      pesoIdeal = (72.7*altura) - 45
  else:
    if (idade <= 40):
      pesoIdeal = (72.7*altura) - 50
    else:
      pesoIdeal = (72.7*altura) - 58   
elif(sexo == "F"):
  if (altura > 1.5):
    pesoIdeal = (62.1*altura) - 44.7
  else:
    if (idade >= 35):
      pesoIdeal = (62.1*altura) - 45
    else:
      pesoIdeal = (62.1*altura) - 49
else:
  print("Sexo diferente de M ou F")

print("Peso Ideal: ", pesoIdeal)
