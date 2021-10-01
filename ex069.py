p = 1
maior = 0
homens = 0
mulheres = 0
while True:
    print(f'--- PESSOA {p} ---')
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Digite o sexo [m/f]: ')).strip().lower()[0]
    print('------------------')
    p+=1
    if(idade >= 18):
        maior += 1
    if(sexo == 'm'):
        homens += 1
    if(sexo == 'f' and idade > 20):
        mulheres += 1
    cont = ' '
    while cont not in 'SsNn':
        cont = str(input('Deseja continuar [s/n]: ')).strip().lower()[0]
    if(cont == 'n'):
        break

print(f'\n{maior} pessoas possuem mais de 18 anos.\nForam cadastrados {homens} homens.\n{mulheres} mulheres possuem menos de 20 anos')
