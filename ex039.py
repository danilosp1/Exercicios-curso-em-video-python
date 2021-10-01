idade = int(input('Digite sua idade: '))

if idade < 18:
    print('Ainda não é hora de se alistar')
elif idade > 18:
    print('Já passou da hora de se alistar.')
else:
    print('É o momento de se alistar!')