val = int(input('Digite o valor da casa: '))
sal = int(input('Digite o salário do comprador: '))
anos = int(input('Digite quantos anos vai pagar: '))

mensal = val/(12*anos)

if(mensal > sal*0.3):
    print('Empréstimo recusado. O valor excede 30% de seu salário. As parcelas seriam de R${:.2f} por mês'.format(mensal))
else:
    print('Emprestimo aceito, as parcelas serão de R${:.2f} por mês.'.format(mensal))