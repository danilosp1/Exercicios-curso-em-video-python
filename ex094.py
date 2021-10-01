individuo = dict()
pessoas, mulheres, acima = [], [], []
soma = 0
while True:
    individuo.clear()
    cont = ' '
    individuo['sexo'] = ' '
    nome = individuo['nome'] = str(input('Nome: '))
    while individuo['sexo'] not in 'MF':
        individuo['sexo'] = str(input('Sexo [M/F]: ')).upper()
    if individuo['sexo'] in 'F':
        mulheres.append(nome)
    individuo['idade'] = int(input('Idade: '))
    soma += individuo['idade']
    pessoas.append(individuo.copy())
    while cont not in 'sn':
        cont = str(input('Deseja continuar? [S/N] ')).lower()[0]
    if cont in 'n': break

media = soma/len(pessoas)
for c in pessoas:
    if c['idade'] > media:
        acima.append(c)

print('=-='*15)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'A média de idade é: {media:.0f}')
print('Mulheres: ', end='')
for i in mulheres:
    print(i, end=' ')
print()
print(f'Pessoas acima da média de idade: ')
for i in acima:
    print(f'    nome = {i["nome"]}; sexo = {i["sexo"]}; idade = {i["idade"]};')
print("<< ENCERRADO >>")