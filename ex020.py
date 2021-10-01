import random

ord = ['', '', '', '']
aluno = [0, 1, 2, 3]
for x in range(4):
    aluno[x] = input('Digite o {}º aluno: '.format(x + 1))
    n = random.randint(0, 3)
    while(ord[n] != ''):
        n = random.randint(0, 3)
    ord[n] = aluno[x]

print('A ordem será: {}, {}, {}, {}'.format(ord[0], ord[1], ord[2], ord[3]))
