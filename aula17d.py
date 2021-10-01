a = [2, 3, 4, 7]
# b = a #ele altera nas duas listas, pois estão igualadas
b = a[:] #assim ele COPIA os valores de A
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')