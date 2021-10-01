time = ('São Paulo', 'Atlético-MG', 'Flamengo',
        'Grêmio', 'Fluminense', 'Internacional',
        'Palmeiras', 'Santos', 'Ceará SC', 'Fortaleza',
        'Corinthians', 'Athletico-PR', 'Bahia',
        'Bragantino', 'Atlético-GO', 'Sport Recife',
        'Vasco da Gama', 'Coritiba', 'Botafogo', 'Goiás')

print(f'Os cinco primeiros colocados são: {time[:5]}')
print(f'Os quatro últimos colocados são: {time[-4:]}')
print(f'Os times organizados em ordem alfabética: {sorted(time)}')
print(f'O Palmeiras está na posição: {time.index("Palmeiras") + 1}')
