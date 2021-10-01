num = input('Digite um número entre 0 e 9999: ')

print('unidade: {}'.format(num[0]))
if(len(num) > 1):
    print('dezena: {}'.format(num[1]))
if(len(num) > 2):
    print('centena: {}'.format(num[2]))
if(len(num) > 3):
    print('milhar: {}'.format(num[3]))
