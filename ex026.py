frase = input('Digite uma frase qualquer: ')
aux = 0

print('A letra "R" aparece {} vezes na frase.'.format(frase.lower().count('r')))
print('Letra "A" aparece pela primeira vez na posição {}.'.format(frase.lower().find('a') + 1))

for x in range(len(frase)):
    if(frase[x].lower() == 'a'):
        aux = x

if(aux > 0): print('Aparece pela ultima vez na posição {}'.format(aux + 1))


