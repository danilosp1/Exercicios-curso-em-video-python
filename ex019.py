import random

aluno = [0, 1, 2, 3]
for x in range(4):
    aluno[x] = input('Digite o {}º aluno: '.format(x + 1))

print('Foi sorteado(a) {}'.format(aluno[random.randint(0, 3)]))
