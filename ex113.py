def leiaint(txt):
    while True:
        try:
            num = int(input(txt))
        except:
            print(f'\033[0;31mErro, entrada incorreta.\033[m')
        else: break
    return num


def leiafloat(txt):
    while True:
        try:
            num = float(input(txt))
        except:
            print(f'\033[0;31mErro, entrada incorreta.\033[m')
        else: break
    return num


n = leiaint('Digite um número inteiro: ')
m = leiafloat('Digite um número decimal: ')
print(f'Você digitou o número {n} e o decimal {m}')
