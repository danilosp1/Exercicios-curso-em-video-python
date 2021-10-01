soma = 0
velho_nome = ''
velho_idade = 0
mulheres_novas = 0
for c in range(0, 4):
    print('----- Pessoa {} -----'.format(c+1))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [m/f]: '))

    if(sexo.lower() == 'm'):
        if (c == 0):
            velho_nome = nome
            velho_idade = idade
        if(idade > velho_idade):
            velho_nome = nome
            velho_idade = idade
    else:
        if(idade < 20):
            mulheres_novas += 1

    soma += idade

media = soma/4

print('\nA média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho do grupo é o {}.'.format(velho_nome))
print('{} mulheres possuem menos de 20 anos.'.format(mulheres_novas))