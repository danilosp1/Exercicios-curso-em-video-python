n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
n = n1
aux = 1
while(aux != 11):
    n = n1 + r*(aux-1)
    print(n, end=' -> ')
    aux += 1
print('fim')
