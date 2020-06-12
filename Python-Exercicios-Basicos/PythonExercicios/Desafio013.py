salário = float(input('Qual é o salário do Funcionário? R$'))
novo = salário + (salário * 15 / 100)
print('O Funcionário que ganhava R${:.2f}, com 15% de de aumento, passa a receber {:.2f}'.format(salário, novo))

