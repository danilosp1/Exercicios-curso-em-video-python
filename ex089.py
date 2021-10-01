alunos, nome, notas = [], [], []

while True:
    cont = ' '
    nome.append(str(input('Nome: ').strip()))
    notas.append(float(input('Primeira nota: ')))
    notas.append(float(input('Segunda nota: ')))
    nome.append(notas[:])
    alunos.append(nome[:])
    notas.clear()
    nome.clear()
    while cont not in 'sn':
        cont = str(input('Deseja continuar? [S/N] ')).lower()[0]
    if cont in 'n': break
print('='*55)
print(f'Nº {"nome":<20}Média')
print('-'*30)
for c, i in enumerate(alunos):
    media = (i[1][0]+i[1][1])/2
    print(f'{c}  {i[0]:<20}{media:>4.1f}')
print('='*55)
while True:
    resp = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if resp == 999: break
    elif resp >= len(alunos):
        print('Aluno não cadastrado, tente novamente.')
    else:
        print(f'Notas de {alunos[resp][0]} são {alunos[resp][1]}')