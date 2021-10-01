lin, matriz = [], []
par = somat = maior = 0
for i in range(1, 4):
    for j in range(1, 4):
        lin.append(int(input(f'Posição [{i}, {j}]: ')))
        if(lin[j - 1]%2 == 0):
            par += lin[j - 1]
        if(j == 3):
            somat += lin[2]
        if(i == 2):
            if(j == 1):
                maior = lin[j - 1]
            else:
                if(lin[j - 1] > maior):
                    maior = lin[j - 1]
    matriz.append(lin[:])
    lin.clear()
print('='*40)
for c, i in enumerate(matriz):
    for j in matriz[c]:
        print(f'[  {j}  ]', end='')
    print()
print('='*40)
print(f'A soma dos valores pares é {par}.')
print(f'A soma dos valores da terceira coluna é {somat}.')
print(f'O maior valor da segunda linha é {maior}.')