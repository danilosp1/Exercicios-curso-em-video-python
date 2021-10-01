sexo = ''
aux = 0
while(aux == 0):
    sexo = str(input('Digite o sexo [m/f]: ')).lower()
    if sexo == 'm' or sexo == 'f':
        aux = 1
    else:
        print('Digitação incorreta, tente novamente.')
print('Voce escolher {}.'.format(sexo))