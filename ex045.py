from random import randint

cont = 's'
while cont == 's':
    print('-----------JOKENPÔ-----------')
    print('[1] pedra')
    print('[2] papel')
    print('[3] tesoura')
    esc = int(input('Qual deseja jogar? '))
    maq = randint(1, 3)

    if(maq == 1):
        aux = 'pedra'
    elif(maq == 2):
        aux = 'papel'
    else:
        aux = 'tesoura'

    if (esc == 1):
        aux2 = 'pedra'
    elif (esc == 2):
        aux2 = 'papel'
    else:
        aux2 = 'tesoura'

    if(maq == esc):
        print('{} x {} : empate'.format(aux2, aux))
    elif((maq == 2 and esc == 1) or (maq == 3 and esc == 2) or (maq == 1 and esc == 3)):
        print('{} x {} : você perdeu'.format(aux2, aux))
    else:
        print('{} x {} : você ganhou!'.format(aux2, aux))

    cont = str(input('Deseja continuar? [s/n] ')).lower()


