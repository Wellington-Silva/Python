    #JOGO
#Faz o computador Pensar
from random import randint
from time import sleep
comp = randint(0, 5)
print("-=-" * 20)
print("Vou pensar em número entre 0 e 5. Tente adivinhar...")
print("CARREGANDO...")
sleep(3)
print("-=-" * 20)

#Jogador tenta adivinhar
jogador = int(input("Adivinhe o número escolhido"))

#Condições
if (jogador == comp):
    print("Você GANHOU")
else:
    print("Você PERDEU. Pensei no número", comp, "e não no número", jogador)
    


