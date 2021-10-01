col, lin = [], []
for i in range(1, 4):
    for j in range(1, 4):
        lin.append(int(input(f'Posição [{i}, {j}]: ')))
    col.append(lin[:])
    lin.clear()
print('='*40)
for c, i in enumerate(col):
    for j in col[c]:
        print(f'[  {j}  ]', end='')
    print()
