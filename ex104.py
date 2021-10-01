def leiaint(txt):
    while True:
        num = input(txt)
        if(num.isnumeric() == False):
            print(f'\033[0;31mErro, número não inteiro válido.\033[m')
        else: break
    return num


n = leiaint('Digite um número inteiro: ')
print(f'Você digitou o número {n}')
