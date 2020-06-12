preço = float(input('Digite o valor do produto:'))
novo = (preço - (preço/100) * 10)
print('O produto que custava {} agora com 10% de desconto vai custar {}'.format(preço, novo))
