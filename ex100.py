from random import randint


def sorteio(lst):
    for cont in range(0, 5):
        lst.append(randint(1, 10))
    print(lst)
    print('='*50)


def somaPar(lst):
    soma = 0
    for c in lst:
        if(c%2 == 0):
            soma += c
    print(f'A soma entre os valores pares de {lst} é {soma}')


números = []
sorteio(números)
somaPar(números)