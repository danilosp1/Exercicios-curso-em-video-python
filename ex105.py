def notas(*num, sit=False):
    '''
    Retorna total, média, menor e maior nota.
    :param num: listagem de notas (aceita várias)
    :param sit: {opcional} situação atual
    :return: dict() -> var
    '''
    lst = dict()
    lst['total'] = len(num)
    lst['maior'] = max(num)
    lst['menor'] = min(num)
    lst['media'] = sum(num)/len(num)
    if(sit):
        if(lst['media'] >= 7):
            situ = 'ÓTIMA'
        elif(lst['media'] >= 5):
            situ = 'RAZOÁVEL'
        else:
            situ = 'RUIM'
        lst['situação'] = situ
    return lst

print(notas(3.5, 2, 6.5, sit=True))