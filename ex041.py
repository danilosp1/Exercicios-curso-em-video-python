idade = int(input('Digite sua idade: '))

if(idade < 9):
    print('Você está categorizado como Mirim.')
elif(idade >= 9 and idade < 14):
    print('Você está categorizado como Infantil.')
elif(idade >= 14 and idade < 19):
    print('Você está categorizado como Junior.')
elif(idade >= 19 and idade < 20):
    print('Você está categorizado como Sênior.')
else:
    print('Você está cateforizado como Master!')