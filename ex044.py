val = float(input('Qual o valor do produto? '))
print('Digite a forma de pagamento:')
print('[1] À vista no dinheiro')
print('[2] À vista no cartão')
print('[3] Até 2x no cartão')
print('[4] 3x ou mais no cartão')
tip = int(input('Qual sua opção de pagamento? '))

if(tip == 1):
    pagamento = val*0.9
elif(tip == 2):
    pagamento = val*0.95
elif(tip == 3):
    pagamento = val
else:
    pagamento = val*1.2

print('Voce pagará no total R${:.2f}'.format(pagamento))