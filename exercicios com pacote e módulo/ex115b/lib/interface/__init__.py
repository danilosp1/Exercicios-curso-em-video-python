c = ('\033[m',         # 0 - sem cor
     '\033[0;31m',  # 1 - vermelho
     '\033[0;32m',  # 2 - verde
     '\033[0;33m',  # 3 - amarelo
     '\033[0;34m',  # 4 - azul
     '\033[0;35m',  # 5 - roxo
     '\033[1;36m'   # 6 - branco
     )


def leiaint(txt):
    while True:
        try:
            num = int(input(txt))
        except:
            print(f'\033[0;31mErro, entrada incorreta.\033[m')
        else: break
    return num


def linha(tam=42):
    return '-'*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[0;33m{c} - \033[0;34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc