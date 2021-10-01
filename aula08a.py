from math import sqrt, ceil, floor
#ou "import math"

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é {:.2f}'.format(num, raiz))
print('A raiz de {} é {}'.format(num, ceil(raiz)))
print('A raiz de {} é {}'.format(num, floor(raiz)))
