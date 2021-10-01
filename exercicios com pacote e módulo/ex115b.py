from ex115b.lib.interface import *
from ex115b.lib.arquivo import *

arq = 'infos.txt'

if not arqExiste(arq):
    criarArq(arq)

while True:
    resposta = menu([ 'Listar Pessoas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        break
    else:
        print(f'{c[1]}Erro, número inválido.{c[0]}')
cabeçalho('>> Programa Encerrado <<')