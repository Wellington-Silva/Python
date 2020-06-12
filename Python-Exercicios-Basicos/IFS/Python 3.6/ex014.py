    # Vaviáveis primárias

#A empresa paga 12 reais por hora e 40$ por dependente
#Sobre salario é feito um desconto de 8,5 para o INSS e 5% para IR
nome = input("Digite o nome do funcionário: ") 
horas = int(input("Digite o nº de horas de trabalho do funcionário:"))
dependentes = int(input("Digite a quantidade de dependentes do fuincionário:"))
    # Calculos
bruto = (12 * horas) + (40 * dependentes)
inss = bruto - ((8.5/100) * bruto)
ir = (5/100) * inss
líquido = 12 * horas
    #Imprimir
print("Nome do funcionário:", nome)
print("Desconto para o INSS: R$", inss)
print("Desonto para o IR: R$",ir)
print("Seu salário líquido é R$", líquido)
