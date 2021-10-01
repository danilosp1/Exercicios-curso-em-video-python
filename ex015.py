km = float(input('Digite a quantidade de Km percorridos: '))
dias = int(input('Digite o número de dias em que o carro foi alugado: '))

val = km*0.15 + dias*60

print('O preço a ser pago é de R${:.2f}'.format(val))