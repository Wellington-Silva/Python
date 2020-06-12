#Variáveis em uma linha
k, r, n = input().split(" ")

#transformação para inteiro
k = int(k)
r = int(r)
n = int(n)

#Atribuições
adiçao = 0
cont = 1

while cont <= n:
  adiçao = adiçao + (cont *  k)
  cont = cont + 1

emprest = adiçao - r

#Avaliação do calculo nas condições
if emprest <= 0:
  print(0)
else:
  print(emprest)


