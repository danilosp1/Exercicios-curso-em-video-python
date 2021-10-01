def contador(*num): #vai gerar uma túpla
    for valor in num:
        tam = len(num)
        print(f'{valor} ', end='')
    print(f'sendo {tam} no total')

contador(2, 1, 7)
contador(8, 8)
contador(4, 4, 7, 6, 2)