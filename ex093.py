jogador = dict()
gol = []
tot_gols = 0
jogador['nome'] = str(input('Nome do jogador: '))
partidas = jogador['total'] = int(input('Partidas jogadas: '))
for i in range(0, partidas):
    gol.append(int(input(f'Quantos gols na partida {i+1}? ')))
    tot_gols += gol[i]
jogador['gols'] = gol[:]
print('=-'*40)
print(jogador)
print('=-'*40)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*40)
print(f'O jogador {jogador["nome"]} jogou {jogador["total"]} partida.')
for i in range(0, partidas):
    print(f'    => Na partida {i+1}, fez {jogador["gols"][i]} gols.')
print(f'Foi um total de {tot_gols} gols.')