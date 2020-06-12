# Maior e Menor
# Faça um programa que leia 3 nº e mostre qual nº é maior e menor
n1 = int(input("Digite um número:"))
n2 = int(input("Digite um número:"))
n3 = int(input("Digite um número:"))
#Verificando quem é MENOR
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#Verificando quem é MAIOR
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n1:
    maior = n3
print("O menor valor digitado foi", menor)
print("O maior valor digitado foi", maior)


