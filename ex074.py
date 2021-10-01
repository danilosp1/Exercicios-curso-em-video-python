from random import randint

t = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in t:
    print(f'{n}', end=' ')
print()
for i in range(0, len(t)):
    if i == 0:
        menor = t[i]
        maior = t[i]
    else:
        if menor > t[i]:
            menor = t[i]
        if maior < t[i]:
            maior = t[i]
print(f'O menor número é: {menor}')
print(f'O maior número é: {maior}')
