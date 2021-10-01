from random import randint

t = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in t:
    print(f'{n}', end=' ')
print()

print(f'O menor número é: {max(t)}')
print(f'O maior número é: {min(t)}')