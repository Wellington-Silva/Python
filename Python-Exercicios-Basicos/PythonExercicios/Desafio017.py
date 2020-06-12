import math
opos = float(input('Comprimento do cateto oposto'))
adj = float(input('Comprimento do cateto adjacente'))
hip = math.hypot(opos, adj)
print('A hipotenusa vai medir {:.2f}'.format(hip))



