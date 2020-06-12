#Algoritmo "Ques3"
#Inicio
ig, ia, en, id, st = input().split()
ig = int(ig)
ia = int(ia)
en = int(en)
id = int(id)
st = int(st)

if (ig == 1) or (ia == 1):
    if (en == 1) and (id == 1):
        if (st == 1):
            print("CORRIGIDO")
        else:
            print("0")

