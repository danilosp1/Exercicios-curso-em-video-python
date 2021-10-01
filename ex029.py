vel = int(input('Digite a velocidade do carro: '))

if(vel > 80):
    multa = (vel - 80)*7
    print('Você foi multado no valor de R${}.00'.format(multa))
else:
    print('Você está dentro do limite de velocidade.')