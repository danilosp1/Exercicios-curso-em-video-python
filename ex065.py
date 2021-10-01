cont = 's'
qt = 0
m = 0
maior = 0
while(cont == 's'):
    n = int(input('Digite um valor: '))
    if(m == 0 or menor > n):
        menor = n
    if(n > maior):
        maior = n
    qt += 1
    m += n
    cont = str(input('Deseja continuar ? [s/n] ')).lower()
media = m/qt
print('\nMaior valor: {}'.format(maior))
print('Menos valor: {}'.format(menor))
print('A média entre os números foi {}'.format(media))
