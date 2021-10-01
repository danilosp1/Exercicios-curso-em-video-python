from ex107 import moeda

p = int(input('Digite um número: '))
print(f'Dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Dobro de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'{moeda.moeda(p)} menos 10% é {moeda.aumentar(p, 10, True)}')
print(f'{moeda.moeda(p)} mais 10% é {moeda.diminuir(p, 10, True)}')