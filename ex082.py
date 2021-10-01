val, par, impar = [], [], []
while True:
    cont = ' '
    n = int(input('Digite um número: '))
    val.append(n)
    if(n%2 == 0):
        par.append(n)
    else:
        impar.append(n)
    while cont not in 'ns':
        cont = str(input('Deseja continuar? [S/N] ')).lower()[0]
    if cont == 'n': break
print(f'Lista digitada: {val}')
print(f'Lista dos pares: {par}')
print(f'Lista dos ímpares: {impar}')