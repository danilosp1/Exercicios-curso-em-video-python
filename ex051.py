n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
n = n1
for c in range(1, 11):
    n = n1 + r*(c-1)
    print(n, end=' -> ')
print('fim')
