peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura**2)

if(imc < 18.5):
    print('Você está abaixo do peso. imc = {}'.format(imc))
elif(imc >= 18.5 and imc < 25):
    print('Você está no peso ideal. imc = {}'.format(imc))
else:
    print('Você está acima do peso. imc = {}'.format(imc))
