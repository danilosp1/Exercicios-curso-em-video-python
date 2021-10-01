ficha = list()

while True:
    cont = ' '
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    while cont not in 'sn':
        cont = str(input('Deseja continuar? [S/N] ')).lower()[0]
    if cont in 'n': break
print('='*55)
print(f'{"Nº":<4}{"NOME":10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')