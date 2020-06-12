#Entrada
quant, custo = input().split()
quant = float(quant)
custo = float(custo)

#Calculos
quanti = quant * 1000
valor = (quanti * custo) 
esgoto = (valor + (0.8 * valor)) + valor
total = valor + esgoto


print("%.2f"%valor)
print("%.2f"%esgoto)
print("%.2f"%total)


