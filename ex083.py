exp = str(input('Digite a expressão: ')).strip()
aberto = fechado = 0
for i in range(0, len(exp)):
    if(exp[i - 1] == '('):
        aberto += 1
    elif(exp[i - 1] == ')'):
        fechado += 1
if(aberto == fechado):
    print('A expressão está correta!')
else:
    print('A expressão está incorreta!')

# esse programa só verifica se tem o mesmo numero de
# parenteses abrindo e fechando, porém não verifica
# posição. O ex083b verifica!