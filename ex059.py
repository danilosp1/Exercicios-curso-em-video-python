menu = 4
while menu != 5:
    if(menu == 4):
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um segundo número: '))
    print('''   ------- MENU -------
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    ------- MENU -------''')
    menu = int(input('Escolha uma opção: '))
    if(menu == 1):
        s = n1 + n2
        print('A soma é {}.'.format(s))
    elif(menu == 2):
        m = n1*n2
        print('A multiplicação é {}.'.format(m))
    elif(menu == 3):
        if(n1 > n2):
            print('{} é maior.'.format(n1))
        elif(n2 > n1):
            print('{} é maior.'.format(n2))
        else:
            print('São iguais.')
    elif(menu == 4): pass
    elif(menu != 5):
        print('Entrada incorreta, digite novamente.')
print('\nFim do programa')
