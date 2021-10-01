# DICIONÁRIOS

pessoas = {'nome': 'Danilo', 'sexo': 'M', 'idade': 17}
print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()

del pessoas['sexo']
pessoas['nome'] = 'André'
pessoas['peso'] = 78.5 #add sem precisar de append

for k, v in pessoas.items():
    print(f'{k} = {v}')