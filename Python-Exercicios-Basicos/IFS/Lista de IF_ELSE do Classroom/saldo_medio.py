saldo = float(input("Saldo Médio:"))
credito = 0

if (saldo < 0):
  print("Saldo Negativo")
elif (saldo <= 200):
  credito = 0
elif (saldo >= 201) and (saldo <= 400):
  credito = (20/100) * saldo
elif (saldo >= 401) and (saldo <= 600):
  credito = (30/100) * saldo
else:
  credito = (40/100) * saldo

print("Saldo: ", saldo)
print("Crédito: ", credito)
    
