from random import randint
from time import sleep

dado = {}
resultado = []
test = []
for c in range(1, 5):
    dado['jogador'] = f'jogador{c}'
    dado['numero'] = randint(1, 6)
    print(f'    O {dado["jogador"]} tirou {dado["numero"]}')
    if c == 1:
        resultado.append(dado.copy())
    else:
        for i in range(0, len(resultado)):
            if dado['numero'] < resultado[i]['numero']:
                resultado.insert(i, dado.copy())
                break
            if i == len(resultado)-1:
                resultado.append(dado.copy())
    sleep(0.5)
print('='*40)
print('Ranking dos jogadores:')
resultado.reverse()
for c in range(0, len(resultado)):
    print(f'    {c+1}º lugar: {resultado[c]["jogador"]} com {resultado[c]["numero"]}')
    sleep(0.5)

