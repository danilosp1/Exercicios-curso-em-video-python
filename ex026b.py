frase = input('Digite uma frase qualquer: ').lower().strip()
aux = 0

print('A letra "R" aparece {} vezes na frase.'.format(frase.count('r')))
print('Letra "A" aparece pela primeira vez na posição {}.'.format(frase.find('a') + 1))
print('Aparece pela ultima vez na posição {}'.format(frase.rfind('a') + 1))


