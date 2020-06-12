preço = float(input('Preço do produto: R$'))
novo = (preço - (preço / 100) * 5)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai ficar R${:.2f}'.format(preço, novo))



