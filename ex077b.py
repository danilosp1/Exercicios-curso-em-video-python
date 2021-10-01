t = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
     'CURTO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
     'MERCADO', 'PROGRAMADOR', 'FUTURO')

for p in t:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')