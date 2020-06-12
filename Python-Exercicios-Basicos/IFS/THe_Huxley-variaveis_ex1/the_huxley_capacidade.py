capacidade = float(input())
tvideo = float(input())
taudio = float(input())
tdados = float(input())
qdmax = ((tvideo*5.2) + (taudio*3.4) + (tdados*1.5)) / capacidade
print(round(qdmax, 2))
