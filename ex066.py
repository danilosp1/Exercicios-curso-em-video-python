s = 0
val = 0
while True:
    n = int(input('Digite um número [999 finaliza]: '))
    if(n == 999):
        break
    val += 1
    s += n
print(f'A soma dos {val} números digitados foi {s}')