n1 = int(input('Digite um valor '))
n2 = int(input('Dgite outro '))
s = n1 + n2
n = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2
print('A soma é {},\no produto é {} \ne a divisão é {:.2f}.'.format(s, n ,d), end=' ')
print('Divisão inteira é {},\nresto é {},\ne potência é {}'.format(di, r, e))
