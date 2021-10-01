l = list()
pos = 0
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    for j in range(0, len(l)):
        if(n < l[j]):
            pos = j
            break
        else:
            pos = j + 1
    if(pos == len(l)):
        print('Adicionado ao final da lista...')
    else:
        print(f'Adicionado na posição {pos} da lista...')
    l.insert(pos, n)
print(l)