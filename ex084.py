entrada, pessoas = [], []
while True:
    ver = ' '
    entrada.append(str(input('Nome: ')).strip())
    entrada.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = entrada[1]
    else:
        if entrada[1] > maior:
            maior = entrada[1]
        if entrada[1] < menor:
            menor = entrada[1]
    pessoas.append(entrada[:])
    entrada.clear()
    while ver not in 'sn':
        ver = str(input('Deseja adicionar mais? [S/N] ')).lower()[0]
    if ver in 'n': break
print('='*40)
print(pessoas)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de ', end='')
for i in pessoas:
    if i[1] == maior:
        print(f'[{i[0]}] ', end='')
print()
print(f'O menor peso foi de {menor:.1f}Kg. Peso de ', end='')
for i in pessoas:
    if i[1] == menor:
        print(f'[{i[0]}] ', end='')

