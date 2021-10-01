maior = 0
for x in range(3):
    n = int(input('Digite o {}º número: '.format(x + 1)))
    if(x == 0): menor = n
    if(n > maior): maior = n
    if(n < menor): menor = n

print('O maior número é o {} e o menor é o {}'.format(maior, menor))