l = []
while True:
    cont = ' '
    l.append(int(input('Digite um número: ')))
    while cont not in 'sn':
        cont = str(input(('Deseja continuar? [S/N] '))).lower()[0]
    if cont in 'n': break
l.sort(reverse=True)
print(f'\nForam digitados {len(l)} números.')
print(f'A lista na ordem descrescente é: {l}')
if 5 in l:
    print('O valor 5 foi digitado e está na lista!')
else:
    print('O valor 5 não está na lista D:')