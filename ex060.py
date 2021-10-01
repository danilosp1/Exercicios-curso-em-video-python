n = int(input('Digite um número para fazer fatorial: '))
print('{}! = '.format(n), end='')
fat = 1
while(n > 1):
    fat *= n
    print('{}x'.format(n), end='')
    n -= 1
print('1 = {}'.format(fat))