c = ('\033[m',         # 0 - sem cor
     '\033[0;31m',  # 1 - vermelho
     '\033[0;32m',  # 2 - verde
     '\033[0;33m',  # 3 - amarelo
     '\033[0;34m',  # 4 - azul
     '\033[0;35m',  # 5 - roxo
     '\033[1;36m'   # 6 - branco
     )


def corp(txt):
    print('-' * 50)
    print(txt.center(50))
    print('-' * 50)


def menu():
    corp('MENU PRINCIPAL')
    print(f'{c[3]}1 - {c[4]}Ver pessoas cadastradas')
    print(f'{c[3]}2 - {c[4]}Cadastrar nova Pessoa')
    print(f'{c[3]}3 - {c[4]}Sair do Sistema{c[0]}')
    print('-' * 50)
    while True:
        try:
            op = int(input('Sua opção: '))
        except:
            print(f'{c[1]}Erro, número inválido.{c[0]}')
        else:
            if(op != 1 and op != 2 and op != 3):
                print(f'{c[1]}Erro, número inválido.{c[0]}')
            else: break
    return op


def ver():
    try:
        arquivo = open('pessoas.txt', 'r')
    except:
        print(f'{c[1]}Não há pessoas cadastradas ainda.{c[0]}')
    else:
        corp('PESSOAS CADASTRADAS')
        for i in arquivo:
            print(i, end='')
        arquivo.close()


def cadastro():
    corp('NOVO CADASTRO')
    nome = str(input('Nome: '))
    while True:
        try:
            idade = int(input('Idade: '))
        except:
            print(f'{c[1]}Erro, valor incorreto{c[0]}')
        else: break
    dado = f'{nome:<30} {idade:>10} anos\n'
    arquivo = open('pessoas.txt', 'a')
    arquivo.write(f'{dado}')
    print(f'Novo registro de {nome} adicionado.')
    arquivo.close()