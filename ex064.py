n = 0
qt = 0
s = 0
while(n != 999):
    n = int(input('Digite um número [999 finaliza]: '))
    if(n != 999):
        qt += 1
        s += n
print('Foram digitados {} números, cuja soma é {}.'.format(qt, s))