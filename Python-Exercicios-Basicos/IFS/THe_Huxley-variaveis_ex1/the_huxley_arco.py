pi = 3.14
raio = float(input())
graus = float(input())
cp_total = 2*pi*raio
cp_arco = graus*cp_total/360
print("%.2f"%cp_arco)
area_total = pi*raio**2
area_setor = (area_total*graus)/360
print("%.2f"%area_setor)

