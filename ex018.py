import math

n = int(input('Digite um ângulo: '))
sin = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tg = math.tan(math.radians(n))

print('O angulo {} tem:\nseno = {:.2f}\ncosseno = {:.2f}\ntangente = {:.2f}'.format(n, sin, cos, tg))