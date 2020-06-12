ig, ia, en, ind, st = input().split()
ig = int(ig)
ia = int(ia)
en = int(en)
ind = int(ind)
st = int(st)

if (ig == 1) or (ia == 1):
  if (en == 1) and (ind == 1):
    if (st == 1):
      print("AVALIADO")
    else:
      print("0")
