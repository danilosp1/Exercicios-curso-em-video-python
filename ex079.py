l = list()
while True:
    cont = ' '
    n = int(input('Digite um valor: '))
    if n not in l:
        l.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Esse número já está no banco de dados.')
    while cont not in 'ns':
        cont = str(input('Quer continuar? [S/N] ')).lower()[0]
    if cont == 'n': break
l.sort()
print(f'Você digitou os valores {l}')