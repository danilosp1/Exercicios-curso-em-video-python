nome = input('Digite seu nome: ').strip()

print(nome.upper())
print(nome.lower())

print('{} letras no total.'.format(len(nome) - nome.count(' ')))

print('O primeiro nome possui {} letras.'.format(len(nome.split()[0])))
