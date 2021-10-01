total = str(input('Digite uma frase: ')).lower()
frase = total.split()
new = len(frase)
word = ''.join(frase)
aux = 0
for c in range(0, len(word)):
    if(word[c] == word[(len(word)-1) - c]):
        aux += 1

# poderia usar 'inverso = word[::-1]' e ficaria mais curto

if(aux == len(word)):
    print('A frase "{}" é um palíndromo!'.format(total))
else:
    print('A frase "{}" não é um palíndromo D:'.format(total))



