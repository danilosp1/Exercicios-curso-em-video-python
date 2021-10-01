exp = str(input('Digite a expressão: ')).strip()
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop() #deleta o ultimo
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão está correta!')
else:
    print('A expressão está incorreta!')
