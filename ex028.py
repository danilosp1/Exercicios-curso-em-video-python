import random

num = random.randint(0, 5)
n = int(input('Digite um número entre 0 e 5: '))

print('Você acertou!' if n == num else 'Você errou :c, o número era {}'.format(num))
