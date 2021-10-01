#TUPLAS

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

#TUPLAS SÃO IMUTÁVEIS
# lanche[1] = 'Refrigerante' -> não funciona

print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[:2])
print(lanche[2:], '\n')

print(len(lanche), '\n')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print()
#ou

for cont in range(0, len(lanche)):
    print(f'Comerei {lanche[cont]} na posição {cont}')
print()
#ou

for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')
print()

print(sorted(lanche)) #coloca em ordem
