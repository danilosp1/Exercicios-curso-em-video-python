def voto(ano):
    from datetime import datetime
    now = datetime.now().year
    i = now - ano
    if(i < 16):
        return 'NEGADO', i
    elif(i >= 16 and i < 18):
        return 'OPCIONAL', i
    else:
        return 'OBRIGATÓRIO', i


n = int(input('Em que ano você nasceu? '))
status = voto(n)
print(f'Com {status[1]} anos: VOTO {status[0]}.')