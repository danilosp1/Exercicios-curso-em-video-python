from time import sleep


def maior(* num):
    print('Analisando os valores passados...')
    for i, c in enumerate(num):
        print(c, end=' ')
        sleep(0.3)
        if(i == 0):
            maior = c
        else:
            if(c > maior):
                maior = c
    print(f'foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

maior(1, 2, 3, 6, 2)

