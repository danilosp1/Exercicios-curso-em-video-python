import random

aluno = [0, 1, 2, 3]
for x in range(4):
    aluno[x] = input('Digite o {}º aluno: '.format(x + 1))
random.shuffle(aluno)
print('A ordem será: ')
print(aluno)