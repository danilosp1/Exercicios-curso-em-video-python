num = list()
for i in range(0, 5):
    num.append(int(input(f'Digite o {i+1}º número: ')))
    if i == 0:
        menor = maior = num[i]
        posmenor = posmaior = str(i)
    else:
        if num[i] < menor:
            menor = num[i]
            posmenor = str(i)
        elif (num[i] == menor):
            posmenor += f'... {i}'
        if num[i] > maior:
            maior = num[i]
            posmaior = str(i)
        elif(num[i] == maior):
            posmaior += f'... {i}'

print(f'Você digitou os valores {num}')
print(f'{maior} é o maior número e está na(s) posição(ões) {posmaior}.')
print(f'{menor} é o menor número e está na(s) posição(ões) {posmenor}.')