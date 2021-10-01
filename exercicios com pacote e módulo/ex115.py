from ex115 import dados


while True:
    entrada = dados.menu()
    if entrada == 1:
        dados.ver()
    elif entrada == 2:
        dados.cadastro()
    else:
        break
dados.corp('>> Programa Encerrado <<')
