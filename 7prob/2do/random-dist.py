#
# select a distribution from random
# produce random numbers on such a distribution
# 
# zeeAlso
# en.wikipedia.org/wiki/Probability_distribution
#
import random

# distribucion triangular
#retorna un numero aleatorio entre 50 y 100 preferentemente mas cerca de 100 (para eso se usa el 90)
print(random.triangular(50, 100, 90))

#retorna un numero aleatorio entre 10 y 40 preferentemente mas cerca de 10 (para eso se usa el 15)
print(random.triangular(10, 40, 15))


# distribucion uniforme
#retorna un numero aleatorio entre 30 y 40
print(random.uniform(30, 40))

#retorna un numero aleatorio entre 30 y 40
print(random.uniform(30, 40))