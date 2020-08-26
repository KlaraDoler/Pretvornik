import bottle
import model
result = ' '
kolicina = 0
st = 0
osnovna = ' '
zelena = ' '


@bottle.get('/')
def prva_stran():
    return bottle.template('prva_stran.tpl', result=result)


@bottle.get('/pretvarjanje_teze/')
def pretvarjanje_teze():
    global kolicina
    kolicina = 'teža'
    return bottle.template('teza.tpl', result=result)


@bottle.get('/pretvarjanje_casa/')
def pretvarjanje_casa():
    global kolicina
    kolicina = 'čas'
    return bottle.template('cas.tpl', result=result)


@bottle.get('/pretvarjanje_dolzine/')
def pretvarjanje_dolzine():
    global kolicina
    kolicina = 'dolžina'
    return bottle.template('dolzina.tpl', result=result)


@bottle.get('/pretvarjanje_temperature/')
def pretvarjanje_temperature():
    global kolicina
    kolicina = 'temperatura'
    return bottle.template('temperatura.tpl', result=result)


@bottle.get('/pretvarjanje_prostornine/')
def pretvarjanje_prostornine():
    global kolicina
    kolicina = 'prostornina'
    return bottle.template('prostornina.tpl', result=result)


@bottle.get('/pretvori/')
def pretvori():
    st = float(bottle.request.query['st'])
    osnovna = bottle.request.query['osnovna']
    zelena = bottle.request.query['zelena']
    result = model.pretvorba(kolicina, st, osnovna, zelena)
    return bottle.template('zadnja_stran.tpl', result=result, st=st, osnovna=osnovna, zelena=zelena)


@bottle.get('/nazaj/')
def nazaj():
    return bottle.template('prva_stran.tpl')


bottle.run(reloader=True, debug=True)
