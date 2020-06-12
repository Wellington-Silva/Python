peso = int(input())
altura = float(input())
imc = (peso/altura)*altura
if (imc == 17):
  print("muito abaixo do peso")
elif (imc == 17) and (18.49):
  print("abaixo do peso")
elif (imc == 18.5) and (24.99):
  print("peso normal")
elif (imc == 25) and (29.99):
  print("acima do peso")
elif (imc == 30) and (34.90):
  print("obesidade")
elif (imc == 35) and (39.99):
  print("obesidade severa")
elif (imc == 40):
  print("obesidade morbida")
