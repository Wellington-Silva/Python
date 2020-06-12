horas = int(input("Digite o valor das horas trabalhadas:"))
vhtra = float(input("Digite o valor das horas trabalhadas:"))
mínimo = float(input("Digite o salário mínimo:"))
extra = int(input("Digite as horas extra:"))
vhext = float(input("Digite o valor das horas extras:"))

htrab = mínimo / 8
hext = mínimo / 4
hextr = extra * vhext
bruto = htrab * vhtra
salário = bruto + vhext

print("Salário a receber: R$", salário)
