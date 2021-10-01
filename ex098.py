from time import sleep


def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print('='*40)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if(i < f):
        while i <= f:
            print(i, end=' ')
            i += p
            sleep(0.1)
    else:
        while i >= f:
            print(i, end=' ')
            i -= p
            sleep(0.1)
    print()


contador(1, 10, 1)
contador(10, 0, -2)
print('='*40)
contador(int(input('inicio: ')),int(input('fim: ')),int(input('passo: ')))