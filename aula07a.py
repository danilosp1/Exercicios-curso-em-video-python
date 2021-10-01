nome = input('Qual seu nome ? ')
a = 3
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))
print('Prazer em te conhecer {:{}^20}!'.format(nome, a))

