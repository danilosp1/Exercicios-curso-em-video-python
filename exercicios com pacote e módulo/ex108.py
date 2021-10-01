from ex107 import moeda

p = int(input('Digite um número: '))
print(f'Dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'{moeda.moeda(p)} menos 10% é {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'{moeda.moeda(p)} mais 10% é {moeda.moeda(moeda.diminuir(p, 10))}')