import random
num = random.randint(0, 10)
aux = 0
tentativas = 0
while aux == 0:
    n = int(input('Adivinhe o número entre 0 e 10 que o computador escolheu: '))
    tentativas += 1
    if(n == num):
        aux = 1
    else:
        print('Número incorreto, tente novamente')

print('Você acertou com {} tentativa(s)! A maquina escolheu o número {}'.format(tentativas, num))
