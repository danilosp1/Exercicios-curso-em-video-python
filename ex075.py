t = (int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')))


print(f'O número 9 aparecu {t.count(9)} vezes.')
if(3 in t):
    print(f'O primeiro número 3 está na posição {t.index(3) + 1}')
else:
    print('Não possui número 3.')

print('os números pares foram: ', end='')
for c in t:
    if(c%2 == 0):
        print(c, end=' ')