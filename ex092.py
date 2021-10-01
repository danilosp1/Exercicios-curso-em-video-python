import datetime

pessoa = dict()
ano_atual = datetime.datetime.now().year

pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = ano_atual-int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if((pessoa['ctps']) != 0):
    pessoa['contratado'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))
    if((ano_atual-pessoa['contratado']) < 35):
        pessoa['aposentadoria'] = (35-(ano_atual-pessoa['contratado']))+pessoa['idade']
    else:
        pessoa['aposentadoria'] = 'aposentado'
    print('-=' * 40)
    print(pessoa)
for k, v in pessoa.items():
    print(f'{k}: {v}')


