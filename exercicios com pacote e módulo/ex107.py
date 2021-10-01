from ex107 import moeda

p = int(input('Digite um número: '))
print(f'Dobro de {p} é {moeda.dobro(p)}')
print(f'Dobro de {p} é {moeda.metade(p)}')
print(f'{p} menos 10% é {moeda.aumentar(p, 10)}')
print(f'{p} mais 10% é {moeda.diminuir(p, 10)}')