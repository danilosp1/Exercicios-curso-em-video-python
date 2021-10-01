maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c+1)))
    if(c == 0):
        menor = peso
    else:
        if(peso < menor):
            menor = peso
        if(peso > maior):
            maior = peso

print('O maior peso foi: {}'.format(maior))
print('O menor peso foi: {}'.format(menor))