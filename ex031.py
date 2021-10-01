dis = int(input('Digite a distância em Km: '))

if(dis <= 200):
    val = dis*0.5
else:
    val = dis*0.45

print('O preço da viagem será de R${:.2f}'.format(val))
