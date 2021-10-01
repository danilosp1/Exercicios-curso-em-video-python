from random import randint
print('='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('='*20)
seq = 0
while True:
    n = ' '
    comp = randint(0, 10)
    val = int(input('Digite um valor: '))
    while n not in 'PpIi':
        n = str(input('Par ou Ímpar? [P/I] ')).strip().lower()[0]
    s = val+comp
    if(s%2 == 0):
        parouimpar = 'deu par!'
        win = 'p'
    else:
        parouimpar = 'deu ímpar!'
        win = 'i'
    print('-'*20, f'\nVocê jogou {val} e o computador {comp}. Total deu {parouimpar}\n', '-'*20)
    if(n == win):
        print('Você venceu!\nVamos jogar novamente...')
        seq += 1
    else:
        print('Você perdeu!')
        break
print(f'GAME OVER! Você venceu {seq} vezes.')



