cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

while True:
    n = int(input('Digite um valor entre 0 e 20: '))
    if(n > 20 or n < 0):
        print('Número inválido, digite novamente')
    else:
        print(f'Você escolheu o número {cont[n]}')
        break


