import math

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = math.sqrt(pow(co, 2) + pow(ca, 2))

print('A hipotenusa de {} e {} é: {:.2f}'.format(co, ca, hi))