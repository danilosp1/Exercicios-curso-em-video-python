def fatorial(num, show=False):
    '''
    -> Calcula o Fatorial de um número
    :param num: O número a ser calculado
    :param show: {opcional} Mostrar ou não a conta
    :return: O valor do fatorial de um número n (str case show=True)
    '''
    fat = 1
    conta = ''
    for c in range(num, 0, -1):
        if(show == True):
            if fat == 1:
                conta = f'{num}'
            else:
                if num >= 1:
                    conta = f'{conta} x {num}'
            result = f'{conta} = {fat}'
        else:
            result = fat
        fat *= c
        num -= 1
    return result


print(fatorial(5, False))
print(help(fatorial))
