    #VIAGEM
viagem = float(input("QUAl a distancia da viagem?"))
print("Você está prestes a começar um viagem de", viagem, "Km/h")
preço = viagem * 0.50 if viagem <= 200 else viagem * 0.45
print("O preço da sua passagem será de R$", preço)

