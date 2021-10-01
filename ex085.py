par, impar, final = [], [], []
for i in range(1, 8):
    n = int(input(f'Digite o {i}º número: '))
    if n%2 == 0:
        par.append(n)
    else:
        impar.append(n)
par.sort()
impar.sort()
final.append(par[:])
final.append(impar[:])
print(final)