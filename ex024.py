cidade = input('Digite o nome da sua cidade: ').strip()

if(cidade.lower().find('santo') == 0):
    print('A cidade {} possui Santo no começo de seu nome.'.format(cidade))
else:
    print('A cidade {} não possui Santo no começo do nome.'.format(cidade))