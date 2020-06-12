esp_interno = str(input("A or C"))
porta_malas = str(input("G or P"))
valor = float(input())
motor = float(input())
cambio = str(input("M or A"))
cont = 1

if (esp_interno == "A"):
    cont = cont+1
if (porta_malas == "G"):
    cont = cont+1
if (valor < 100.000):
    cont = cont+1
if (motor >= 1.5 ):
    cont = cont+1
if (cambio == "A"):
    cont = cont+1
if (cont >= 2):
    print("Boa compra.")
if (cont ==1):
    print("Pode ser uma opção.")
if (cont < 1):
    print("Não compre!")
