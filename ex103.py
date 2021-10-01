def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

nome = str(input('Nome: ')).strip()
gols = str(input('Gols: ')).strip()
if nome == '' and gols.isnumeric() == False:
    ficha()
elif nome == '' and gols.isnumeric() == True:
    ficha(gols=int(gols))
elif nome != '' and gols.isnumeric() == False:
    ficha(nome)
else:
    ficha(nome, int(gols))