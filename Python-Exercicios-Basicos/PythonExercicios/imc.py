altura = float("Altura: ")
sexo = str("Altura: ")

idealman = ((72.7 * altura) - 58)
idealwoman = ((62.1 * altura) - 44.7)

if(sexo == "M"):
  print("Seu peso ideal é: ", idealman)
elif(sexo == "F"):
  print("Seu peso ideal é: ", idealwoman)
