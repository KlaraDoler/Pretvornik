#TEŽA
#Pretvarjanje teže v osnovno enoto (g)


def teza_osnovna(st, enota):
    if enota == 't':
        return st * 100000
    elif enota == 'kg':
        return st * 1000
    elif enota == 'dag':
        return st * 10
    elif enota == 'g':
        return st
    elif enota == 'mg':
        return st / 1000
    elif enota == 'lb':
        return st * 453.59237
    elif enota == 'oz':
        return st * 28.34949
    else:
        return 'Napaka'

#Pretvarjanje teže v želeno enoto


def teza_zelena(st, enota):
    if enota == 't':
        return st / 100000
    elif enota == 'kg':
        return st / 1000
    elif enota == 'dag':
        return st / 10
    elif enota == 'g':
        return st
    elif enota == 'mg':
        return st * 1000
    elif enota == 'lb':
        return st / 453.59237
    elif enota == 'oz':
        return st / 28.34949
    else:
        return 'Napaka'


def teza(st, osnovna, zelena):
    v_osnovno = teza_osnovna(st, osnovna)
    rezultat = teza_zelena(v_osnovno, zelena)
    return rezultat


#ČAS
#Pretvarjanje časa v osnovno enoto (h)


def cas_osnovna(st, enota):
    if enota == 'leto':
        return st * 8760
    elif enota == 'dan':
        return st * 24
    elif enota == 'h':
        return st
    elif enota == 'min':
        return st / 60
    elif enota == 's':
        return st / 3600
    else:
        return 'Napaka'

#Pretvarjanje časa v želeno enoto


def cas_zelena(st, enota):
    if enota == 'leto':
        return st / 8760
    elif enota == 'dan':
        return st / 24
    elif enota == 'h':
        return st
    elif enota == 'min':
        return st * 60
    elif enota == 's':
        return st * 3600
    else:
        return 'Napaka'


def cas(st, osnovna, zelena):
    v_osnovno = cas_osnovna(st, osnovna)
    rezultat = cas_zelena(v_osnovno, zelena)
    return rezultat


#DOLŽINA
#Pretvarjanje dolžine v osnovno enoto (m)


def dolzina_osnovna(st, enota):
    if enota == 'km':
        return st * 1000
    elif enota == 'm':
        return st
    elif enota == 'dm':
        return st / 10
    elif enota == 'cm':
        return st / 100
    elif enota == 'mm':
        return st / 1000
    elif enota == 'milja':
        return st * 0.00062137
    elif enota == 'yd':
        return st * 1.0936
    elif enota == 'in':
        return st / 39.370
    elif enota == 'ft':
        return st / 3.2808
    else:
        return 'Napaka'

#Pretvarjanje dolžine v želeno enoto


def dolzina_zelena(st, enota):
    if enota == 'km':
        return st / 1000
    elif enota == 'm':
        return st
    elif enota == 'dm':
        return st * 10
    elif enota == 'cm':
        return st * 100
    elif enota == 'mm':
        return st * 1000
    elif enota == 'milja':
        return st / 0.00062137
    elif enota == 'yd':
        return st / 1.0936
    elif enota == 'in':
        return st * 39.370
    elif enota == 'ft':
        return st * 3.2808
    else:
        return 'Napaka'


def dolzina(st, osnovna, zelena):
    v_osnovno = dolzina_osnovna(st, osnovna)
    rezultat = dolzina_zelena(v_osnovno, zelena)
    return rezultat


#TEMPERATURA
#Pretvarjanje temperature v osnovno enoto (K)


def temperatura_osnovna(st, enota):
    if enota == 'K':
        return st
    elif enota == 'C':
        return st + 273.15
    elif enota == 'F':
        return (st + 459.67) * 5 / 9
    else:
        return 'Napaka'

#Pretvarjanje temperature v želeno enoto


def temperatura_zelena(st, enota):
    if enota == 'K':
        return st
    elif enota == 'C':
        return st - 273.15
    elif enota == 'F':
        return st * 5 / 9 - 459.67
    else:
        return 'Napaka'


def temperatura(st, osnovna, zelena):
    v_osnovno = temperatura_osnovna(st, osnovna)
    rezultat = temperatura_zelena(v_osnovno, zelena)
    return rezultat


#PROSTORNINA
#Pretvarjanje prostornine v osnovno enoto (l)


def prostornina_osnovna(st, enota):
    if enota == 'hl':
        return st * 100
    elif enota == 'l':
        return st
    elif enota == 'dl':
        return st / 10
    elif enota == 'cl':
        return st / 100
    elif enota == 'ml':
        return st / 1000
    else:
        return 'Napaka'

#Pretvarjanje prostornine v želeno enoto


def prostornina_zelena(st, enota):
    if enota == 'hl':
        return st / 100
    elif enota == 'l':
        return st
    elif enota == 'dl':
        return st * 10
    elif enota == 'cl':
        return st * 100
    elif enota == 'ml':
        return st * 1000
    else:
        return 'Napaka'


def prostornina(st, osnovna, zelena):
    v_osnovno = prostornina_osnovna(st, osnovna)
    rezultat = prostornina_zelena(v_osnovno, zelena)
    return rezultat


####


def pretvorba(kolicina, st, osnovna, zelena):
    if kolicina == 'teža':
        return teza(st, osnovna, zelena)
    elif kolicina == 'dolžina':
        return dolzina(st, osnovna, zelena)
    elif kolicina == 'čas':
        return cas(st, osnovna, zelena)
    elif kolicina == 'temperatura':
        return temperatura(st, osnovna, zelena)
    elif kolicina == 'prostornina':
        return prostornina(st, osnovna, zelena)
