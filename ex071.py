cinq = vint = dez = um = 0
val = int(input('Digite o valor que deseja sacar: R$'))
while True:
    if(val-50 > 0):
        cinq += 1
        val -= 50
    elif(val-20 > 0):
        vint += 1
        val -= 20
    elif(val-10 > 0):
        dez += 1
        val -= 10
    elif(val-1 > 0):
        um += 1
        val -= 1
    else: break
print(f'Total de {cinq} cédulas de R$50')
print(f'Total de {vint} cédulas de R$20')
print(f'Total de {dez} cédulas de R$10')
print(f'Total de {um} cédulas de R$1')