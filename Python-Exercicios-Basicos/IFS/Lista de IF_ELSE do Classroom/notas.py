n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
faltas = int(input("Faltas: "))
media = ((n1*3)+(n2*2)+(n3*5))/3

if (media < 6.0):
  print("Reprovado")
elif (media >= 6.0) and (faltas < 20):
  print("Aprovado")
else:
  print("Reprovado")
  
