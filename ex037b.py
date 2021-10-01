import math

num = int(input('Digite um número: '))
print('---------------------------------')

print('[1] Binário')
print('[2] Octal')
print('[3] Hexadecimal')

conv = int(input('Digite a base de conversão: '))

if conv == 1:
    print('O número em binário é: {}'.format(bin(num)[2:]))
elif conv == 2:
    print('O número em octal é: {}'.format(oct(num)[2:]))
else:
    print('O número em hexadecimal é: {}'.format(hex(num)[2:]))

