val, par, impar = [], [], []
while True:
    cont = ' '
    val.append(int(input('Digite um número: ')))
    while cont not in 'ns':
        cont = str(input('Deseja continuar? [S/N] ')).lower()[0]
    if cont == 'n': break
for i in val:
    if i%2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(f'Lista digitada: {val}')
print(f'Lista dos pares: {par}')
print(f'Lista dos ímpares: {impar}')