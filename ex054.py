import datetime

maior = 0
data = datetime.datetime.now()
for c in range(0, 7):
    idade = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c+1)))
    if(data.year - idade >= 18):
        maior += 1
print('{} pessoas são de maior!'.format(maior))