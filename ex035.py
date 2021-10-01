reta = [0,0,0]
aux = 0
for x in range(3):
    reta[x] = int(input('Digite o {}º comprimento: '.format(x + 1)))

for x in range(3):
    if(x != 2):
        if (reta[x] > reta[x + 1]):
            aux = reta[x]
            reta[x] = reta[x + 1]
            reta[x + 1] = aux
    else:
        if (reta[0] > reta[x-1]):
            aux = reta[x-1]
            reta[x-1] = reta[0]
            reta[0] = aux

if(reta[0] + reta[1] > reta[2]):
    print('Pode formar um triângulo!')
else:
    print('Não é possível formar um triângulo.')
