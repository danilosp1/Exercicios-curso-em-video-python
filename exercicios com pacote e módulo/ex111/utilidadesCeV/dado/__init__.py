def leiadinheiro(txt):
    while True:
        val = input(txt)
        if val.isnumeric():
            ret = val
            break
        else:
            if val.find('.') != -1:
                ret = val.replace('.', '')
                if ret.isnumeric():
                    ret = int(ret) / (10**(len(ret) - val.find('.')))
                    break
            elif val.find(',') != -1:
                ret = val.replace(',', '')
                if ret.isnumeric():
                    ret = int(ret) / (10**(len(ret) - val.find(',')))
                    break
            print(f'\033[0;31mERRO: "{val}" é um preço inválido\033[m')
    return float(ret)


# FORMA SIMPLIFICADA
def leiamoney(txt):
    while True:
        val = input(txt).replace(',', '.').strip()
        if val.isalpha() or val.isalnum() or val == '':
            print(f'\033[0;31mERRO: "{val}" é um preço inválido\033[m')
        else:
            break
    return float(val)