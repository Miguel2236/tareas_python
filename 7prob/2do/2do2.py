#
# 2do
#
import random

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

# llamar a la funcion volado
print(volado())