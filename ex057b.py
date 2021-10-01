sexo = str(input('Digite o sexo [m/f]: ')).strip().lower()[0]
while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido, informe novamente: ')).strip().lower()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
