num = [2, 5, 9, 2, 1]
num[2] = 3
print(num,'\n')

num.append(7) #adiciona um novo espaço
print(num,'\n')

num.sort() #coloca em ordem
print(num,'\n')

num.sort(reverse=True)
print(num,'\n')

print(f'Essa lista tem {len(num)} elementos.')

num.insert(2, 0) #adiciona o 0 na posição 2 e realoca o resto
print(num,'\n')

num.pop() #remove o ultimo elemento
print(num,'\n')

num.pop(2) #remove o elemento na posição 2
print(num,'\n')

if 2 in num:
    num.remove(2) #remove o primeiro numero 2 que tiver
print(num,'\n')

