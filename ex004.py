n = input('Digite algo: ')

print('É do tipo {}'.format(type(n)))
print('É numérico ? {}'.format(n.isnumeric()))
print('É alfanumérico ? ? {}'.format(n.isalnum()))
print('É alfabético ? {}'.format(n.isalpha()))
print('É decimal ? {}'.format(n.isdecimal()))
print('É printável ? {}'.format(n.isprintable()))
print('É identificador ? {}'.format(n.isidentifier()))
print('É minusculo ? {}'.format(n.islower()))
print('Possui apenas espaço ? {}'.format(n.isspace()))
print('É maiusculo ? {}'.format(n.isupper()))
print('É um digito ? {}'.format(n.isdigit()))