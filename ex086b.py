matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = (int(input(f'Posição [{i}, {j}]: ')))
print('='*40)
for i in matriz:
    for j in i:
        print(f'[  {j}  ]', end='')
    print()