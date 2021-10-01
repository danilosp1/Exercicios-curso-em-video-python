print('\033[7;31;40mOlá mundo!\033[m')
print('\033[7;30mOlá Mundo!\033[m')
a = 5
b = 8

print('Os valores são \033[1;36;40m{}\033[m e \033[1;31;45m{}\033[m!!!'.format(a, b))

nome = 'Danilo'
print('Muito prazer em te conhecer, {}{}{}'.format('\033[4;32m', nome, '\033[m'))
# \033[(0, 1, 4, 7);(30 à 37);(40 à 47)m
# \033[(formatação;texto;fundo)m