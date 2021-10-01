t = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
     'CURTO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
     'MERCADO', 'PROGRAMADOR', 'FUTURO')

for c in range(0, len(t)):
    a = e = i = o = u = ''
    for n in range(0, len(t[c])):
        if t[c][n] in 'aA':
            a += 'a '
        elif t[c][n] in 'eE':
            e += 'e '
        elif t[c][n] in 'iI':
            i += 'i '
        elif t[c][n] in 'oO':
            o += 'o '
        elif t[c][n] in 'uU':
            u += 'u '
    print(f'Na palavra {t[c].upper()} temos {a}{e}{i}{o}{u}')