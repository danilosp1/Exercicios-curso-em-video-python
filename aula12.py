name = str(input('Digite seu nome: '))

if(name == 'Danilo'):
    print('Que nome bonito!')
elif(name == 'Pedro' or name == 'Maria'):
    print('Seu nome é bem popular no Brasil.')
elif(name in 'Ana Cláudia Jésica Juliana'):
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')

print('Tenha um bom dia {}'.format(name))
