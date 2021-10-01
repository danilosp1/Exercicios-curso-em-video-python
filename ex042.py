r = [0,0,0]
for x in range(3):
    r[x] = int(input('Digite o {}º comprimento: '.format(x+1)))

if r[0] < r[1] + r[2] and r[1] < r[2] + r[0] and r[2] < r[1] + r[0]:
    print('Pode formar um triângulo!')
    if(r[0] == r[1] and r[0] == r[2]):
        print('É equilátero!')
    elif(r[0] == r[1] or r[0] == r[2] or r[1] == r[2]):
        print('É isósceles!')
    else:
        print('É escaleno!')
else:
    print('Não pode formar um triângulo.')