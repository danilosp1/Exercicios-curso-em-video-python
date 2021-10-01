valor = [[], []]
for i in range(1, 8):
    n = int(input(f'Digite o {i}º número: '))
    if n%2 == 0:
        valor[0].append(n)
    else:
        valor[1].append(n)
valor[0].sort()
valor[1].sort()
print(valor)