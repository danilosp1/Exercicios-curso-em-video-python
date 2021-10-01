import math

aux = ''
aux2 = ''
n = 1

num = int(input('Digite um número: '))
numero = num
print('---------------------------------')

print('[1] Binário')
print('[2] Octal')
print('[3] Hexadecimal')

conv = int(input('Digite a base de conversão: '))

if(conv == 1):
    while(n == 1):
        aux = str(num%2)
        aux2 = aux + aux2
        num = int(num/2)
        if(num//2 == 0):
            aux = str(num % 2)
            aux2 = aux + aux2
            num = int(num / 2)
            n = 2
    print('Número {} em binário: {}'.format(numero, aux2))
elif(conv == 2):
    while (n == 1):
        aux = str(num % 8)
        aux2 = aux + aux2
        num = int(num / 8)
        if (num // 8 == 0):
            aux = str(num % 8)
            aux2 = aux + aux2
            num = int(num / 8)
            n = 2
    print('Número {} em octal: {}'.format(numero, aux2))
else:
    while (n == 1):
        aux = str(num % 16)
        if(aux == '10'): aux='A'
        elif(aux == '11'): aux='B'
        elif (aux == '12'):aux = 'C'
        elif (aux == '13'): aux = 'D'
        elif (aux == '14'): aux = 'E'
        elif (aux == '15'): aux = 'F'
        else: pass
        aux2 = aux + aux2
        num = int(num / 16)
        if (num // 16 == 0):
            aux = str(num % 16)
            if (aux == '10'): aux = 'A'
            elif (aux == '11'): aux = 'B'
            elif (aux == '12'): aux = 'C'
            elif (aux == '13'): aux = 'D'
            elif (aux == '14'): aux = 'E'
            elif (aux == '15'): aux = 'F'
            else: pass
            aux2 = aux + aux2
            num = int(num / 16)
            n = 2
    print('Número {} em hexadecimal: {}'.format(numero, aux2))