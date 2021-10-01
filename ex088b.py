from random import randint
import time

jogos, num = [], []
qnt = int(input('Quantos jogos serão gerados? '))
for i in range(0, qnt):
    for j in range(0, 6):
        while True:
            n = randint(1, 60)
            if n not in num:
                num.append(n)
                break
    num.sort()
    jogos.append(num[:])
    num.clear()
print('='*40)
for v, c in enumerate(jogos):
    print(f'Jogo {v+1}: {c}')
    time.sleep(1)