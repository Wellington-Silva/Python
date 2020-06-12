from math import radians, sin, cos, tan   #Necessário colocar em Radianos
n = float(input('Digite o que você deseja:'))
sen = sin(radians(n))
cos = cos(radians(n))
tan = tan(radians(n))
print('O ângulo de {} tem o SENO de {:.2f}'.format(n, sen))
print('O ângulo de {} tem o COSCENO de {:.2f}'.format(n, cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(n, tan))

