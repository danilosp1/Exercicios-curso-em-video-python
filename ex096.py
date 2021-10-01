def area(l, c):
    print(f'A área do terreno {l}x{c} é {l*c:.1f} m².')

print('Controle de terrenos')
print('-'*15)

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)