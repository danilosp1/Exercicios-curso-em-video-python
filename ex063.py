n = int(input('Digite quantos termos de Fibonnaci deseja: '))
a1 = 0
a2 = 1
while(n > 0):
    if(n == 1):
        print(a1)
    else:
        print(a1, end=' -> ')
    aux = a1
    a1 += a2
    a2 = aux
    n -= 1

