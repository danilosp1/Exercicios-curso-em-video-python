sal = int(input('Digite seu salário: '))

if(sal > 1250):
    aum = 1.1
else:
    aum = 1.15

novoSal = sal*aum
print('Seu salário passou a ser R${:.2f} com um aumento de {:.0f}%'.format(novoSal, (aum - 1)*100))