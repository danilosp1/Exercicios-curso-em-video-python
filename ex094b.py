individuo = dict()
pessoas = []
soma = 0
while True:
    individuo.clear()
    cont = ' '
    individuo['sexo'] = ' '
    nome = individuo['nome'] = str(input('Nome: '))
    while individuo['sexo'] not in 'MF':
        individuo['sexo'] = str(input('Sexo [M/F]: ')).upper()
    individuo['idade'] = int(input('Idade: '))
    soma += individuo['idade']
    pessoas.append(individuo.copy())
    while cont not in 'sn':
        cont = str(input('Deseja continuar? [S/N] ')).lower()[0]
    if cont in 'n': break
media = soma/len(pessoas)
print('=-='*15)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'A média de idade é: {media:.0f}')
print('Mulheres: ', end='')
for i in pessoas:
    if(i['sexo'] in 'F'):
        print(f'{i["nome"]} ', end='')
print()
print(f'Pessoas acima da média de idade: ')
for i in pessoas:
    if(i['idade'] > media):
        print(f'    nome = {i["nome"]}; sexo = {i["sexo"]}; idade = {i["idade"]};')
print("<< ENCERRADO >>")