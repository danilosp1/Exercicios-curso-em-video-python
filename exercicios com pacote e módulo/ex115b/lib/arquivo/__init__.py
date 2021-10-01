from ex115b.lib.interface import *

c = ('\033[m',         # 0 - sem cor
     '\033[0;31m',  # 1 - vermelho
     '\033[0;32m',  # 2 - verde
     '\033[0;33m',  # 3 - amarelo
     '\033[0;34m',  # 4 - azul
     '\033[0;35m',  # 5 - roxo
     '\033[1;36m'   # 6 - branco
     )


def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        return False
    else:
        return True


def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ERRO: O arquivo não foi criado.')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'{c[1]}Erro ao ler o arquivo.{c[0]}')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print(f'{c[1]}Erro ao abrir o arquivo.{c[0]}')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(f'{c[1]}Houve um ERRO na hora de escrever os dados!{c[0]}')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()