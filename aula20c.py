def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

soma(3, 4, 6, 1)