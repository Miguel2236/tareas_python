#
# 2do
#
import random

# funcion para determinar un punto cardinal usando un numero random
# se genera un numero aleatorio y se valida en alguno de los 4 rangos
def brujula(semilla):

    msg = ''

    if(semilla >= 0 and semilla < 9):
        msg = 'Norte'

    if(semilla >= 10 and semilla < 19):
        msg = 'Sur'

    if(semilla >= 20 and semilla < 29):
        msg = 'Este'

    if(semilla >= 30 and semilla <= 40):
        msg = 'Oeste'

    return msg

# funcion de volado, se tira una moneda y se determina cuantas veces cayó en cada cara
# se lanza la modena 1000 veces y usando eloperando modulo se verifica la cara de la moneda
# se contabiliza el numero de cada cara y se muestra en un mensaje
def volado():

    msg     = ''

    cara    = 0

    sello   = 0

    i       = 0

    while i < 1000:

        semilla = random.randrange(0,10)

        if(semilla % 2 == 0):
            cara = cara + 1
            
        if(semilla % 2 == 1):
            sello = sello + 1

        i = i + 1

    msg = "Cara cayo ",cara," veces y sello cayo ",sello," veces."

    return msg


# llamar a la funcion brujula enviando un valor aleatorio en un rango de 0 a 40
print(brujula(random.randrange(0,40)))

# llamar a la funcion volado
print(volado())