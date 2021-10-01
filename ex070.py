gasto = 0
maior = 0
while True:
    nome = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o preço do produto: '))
    print('='*10)
    if(gasto == 0):
        barato = valor
        barato_nome = nome
    elif(valor < barato):
        barato = valor
        barato_nome = nome
    gasto += valor
    if(valor > 1000):
        maior += 1
    cont = ' '
    while cont not in 'SsNn':
        cont = str(input('Deseja continuar ? [s/n] ')).strip().lower()[0]
    if(cont == 'n'): break
print(f'Foi gasto no total R${gasto:.2f}\n{maior} produtos custam mais de R$1000.00\n{barato_nome} é o produto mais barato')