n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
m = (n1+n2)/2

if(m < 5):
    print('Reprovado!')
elif(m >= 5 and m < 7):
    print('Recuperação!')
else:
    print('Aprovado!')