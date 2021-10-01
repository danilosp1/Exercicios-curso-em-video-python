frase = 'Curso em Video Python'
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[::3], '\n')

print("""texto grande simulado
no role pra ver como funciona usando aspas 
triplas pra dividir :D \n""")

print(frase.upper().count('O'))
print(len(frase.strip())) #strip remove espaços antes e depois

print(frase.lower().replace('python', 'Android'))

print('Curso' in frase)
print(frase.lower().find('video')) #posição inicial onde está

dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[2][3]) #pegou a terceira letra do segundo