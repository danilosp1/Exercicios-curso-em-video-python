# -*- coding: utf-8 -*-

val = float(input())
total = val
ced = 100
totced = 0
tipo = 'nota'
print('NOTAS:')
while True:
    if(total >= ced):
        total -= ced
        totced += 1
    else:
        print(f'{totced} {tipo}(s) de R$ {ced:.2f}')
        if(ced == 100):
            ced = 50
        elif(ced == 50):
            ced = 20
        elif(ced == 20):
            ced = 10
        elif(ced == 10):
            ced = 5
        elif(ced == 5):
            ced = 2
        elif(ced == 2):
            ced = 1
            print('MOEDAS:')
            tipo = 'moeda'
        elif(ced == 1):
            ced = 0.50
        elif(ced == 0.50):
            ced = 0.25
        elif(ced == 0.25):
            ced = 0.10
        elif(ced == 0.10):
            ced = 0.05
        elif(ced == 0.05):
            ced = 0.01
        else: break
        totced = 0