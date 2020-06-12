i = int(input("Digite i:"))
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
maior1 = 0
maior2 = 0
maior3 = 0

if (a > b) and (a > c):
  maior1 = a
  if (b > c):
    maior2 = b
    maior3 = c
  else:
    maior2 = c
    maior3 = b
elif (b > a) and (b > c):
  maior1 = b
  if (a > c):
    maior2 = a
    maior3 = c
  else:
    maior2 = c
    maior3 = a
else:
  maior1 = c
  if (a > b):
    maior2 = a
    maior3 = b
  else:
    maior2 = b
    maior3 = a
#Testando a variável i
if (i == 1):
  print("Crescente: ", maior3, maior2, maior1)
elif (i == 2):
  print("Decrescente: ", maior1, maior2, maior3)
else:
  print("Maior no meio: ", maior2, maior1, maior3)
  
