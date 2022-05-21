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

# llamar a la funcion brujula enviando un valor aleatorio en un rango de 0 a 40
print(brujula(random.randrange(0,40)))