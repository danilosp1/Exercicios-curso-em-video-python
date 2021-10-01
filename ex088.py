from random import randint
import time

jogos, num = [], []
qnt = int(input('Quantos jogos serão gerados? '))
for i in range(0, qnt):
    for j in range(0, 6):
        num.append(randint(1, 60))
        n = num[j]
        for c in range(0, len(num) - 1):
            while n == num[c]:
                num.pop(-1)
                num.append(randint(1, 60))
                n = num[j]
    num.sort()
    jogos.append(num[:])
    num.clear()
print('='*40)
for v, c in enumerate(jogos):
    print(f'Jogo {v+1}: {c}')
    time.sleep(1)