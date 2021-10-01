while True:
    n = int(input('Digite um número [negativo encerra]: '))
    if(n < 0):
        break
    for c in range(1, 11):
        m = n*c
        print(f'{n} x {c} = {m}')
print('Programa encerrado')