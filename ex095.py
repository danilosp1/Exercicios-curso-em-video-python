jogador = dict()
time = []
gol = []
tot_gols = 0
while True:
    cont = ' '
    tot_gols = 0
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = jogador['total'] = int(input('Partidas jogadas: '))

    for i in range(0, partidas):
        gol.append(int(input(f'Quantos gols na partida {i+1}? ')))
        tot_gols += gol[i]
    jogador['totgols'] = tot_gols
    jogador['gols'] = gol[:]
    gol.clear()
    jogador['cod'] = len(time)
    time.append(jogador.copy())

    while cont not in 'sn':
        cont = str(input('Deseja continuar? [S/N] ')).lower()[0]
    if cont in 'n': break

print('=-'*40)
print(f'{"cod":<4}{"nome":<15}{"gols":<15}{"total":<15}')
print('-'*40)
gols = "gols"
for i in time:
    print(f'{(i["cod"]):>3} {(i["nome"]):<15}{f"{i[gols]}":<15}{(i["totgols"]):<15}')
print('=-'*40)
while True:
    escolha = int(input('Mostrar dados de qual jogador? [999 encerra] '))
    if(escolha == 999): break
    if(escolha >= len(time)):
        print(f'ERRO! Não existe jogador com código {escolha}! Tente novamente.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR: {time[escolha]["nome"]}')
        for i, g in enumerate(time[escolha]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('=-'*40)
print('>>> PROGRAMA ENCERRADO <<<')