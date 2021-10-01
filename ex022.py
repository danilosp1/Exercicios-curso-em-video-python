nome = input('Digite seu nome: ')

print(nome.upper())
print(nome.lower())

esp = ''.join(nome.strip().split())
print('{} letras no total.'.format(len(esp)))

print('O primeiro nome possui {} letras.'.format(len(nome.split()[0])))
