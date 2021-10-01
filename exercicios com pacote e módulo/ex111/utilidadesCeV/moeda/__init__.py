def aumentar(n, aum, m=False):
    val = n + (n * (aum / 100))
    if m:
        val = moeda(val)
    return val


def diminuir(n, aum, m=False):
    val = n - (n * (aum / 100))
    if m:
        val = moeda(val)
    return val


def dobro(n, m=False):
    val = n * 2
    if m:
        val = moeda(val)
    return val


def metade(n, m=False):
    val = n / 2
    if m:
        val = moeda(val)
    return val


def moeda(n=0, moeda='R$'):
    val = f'{moeda}{n:.2f}'.replace('.', ',')
    return val


def resumo(n, aum=0, dim=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{aum}% de aumento: \t{aumentar(n, aum, True)}')
    print(f'{dim}% de redução: \t{diminuir(n, dim, True)}')
    print('-' * 30)
