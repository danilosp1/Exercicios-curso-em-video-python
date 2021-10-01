n = int(input('Digite um número: '))
aux = 0

for c in range(1, n+1):
    if(n != 1 and n%c == 0):
        aux += 1
if(aux == 2):
    print('O número {} é primo!'.format(n))
else:
    print('O número {} não é primo!'.format(n))