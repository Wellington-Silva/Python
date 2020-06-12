ataque = input()
defesa = input()

if (ataque == defesa):
  print("Empate")
elif (ataque == "Plantas"):
  if (defesa == "Fogo"):
    print("Desvantagem")
  else:
    print("Vantagem")
elif (ataque == "Fogo"):
  if (defesa == "Agua"):
    print("Desvantagem")
  else:
    print("Vantagem")
elif (ataque == "Agua"):
  if (defesa == "Planta"):
    print("Desvantagem")
  else:
    print("Vantagem")
    
  

