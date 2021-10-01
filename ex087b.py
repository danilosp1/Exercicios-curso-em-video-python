matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = impar = somat = maior = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = (int(input(f'Posição [{i+1}, {j+1}]: ')))
        if matriz[i][j]%2 == 0:
            par += matriz[i][j]
        if (j == 2):
            somat += matriz[i][2]
        if (i == 2):
            if (j == 1):
                maior = matriz[i][j]
            else:
                if (matriz[i][j] > maior):
                    maior = matriz[i][j]
print('='*40)
for i in matriz:
    for j in i:
        print(f'[  {j}  ]', end='')
    print()
print('='*40)
print(f'A soma dos valores pares é {par}.')
print(f'A soma dos valores da terceira coluna é {somat}.')
print(f'O maior valor da segunda linha é {maior}.')