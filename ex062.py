n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
n = 0
cont = 1
max = 10
c = 1
while(cont != 0):
    while c <= max:
        n = n1 + r*(c-1)
        print(n, end=' -> ')
        c += 1
    print('...')
    cont = int(input('Deseja mais quantos números ? '))
    max += cont