c = ('\033[m',         # 0 - sem cor
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[1;30;47m'   # 6 - branco
     )


def ajuda(cmd):
    titulo(f'Acessando o manual do comando \'{cmd}\'', 4)
    print(c[6], end='')
    print(help(cmd))
    print(c[0])

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    command = str(input('Digite o comando [FIM encerra]: ')).strip()
    if command.upper() == 'FIM':
        print('>> Programa finalizado <<')
        break
    else:
        ajuda(command)
titulo('ATÉ LOGO!', 1)

