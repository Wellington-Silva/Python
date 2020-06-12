salario = float(input())
extra = int(input())
extra1 = salario/44
extra2 = (extra1 * (0.1 * extra1)) + salario
final = salario + extra2
print("%.2f"%final)
