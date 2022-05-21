#
# generate a function to produce points
# to be used as x-axis
#
# INPUT
# -> a initial point
# -> b final point
# -> c increment
#
# OUTPUT
# <- list of points
#
# for instance for this range [1,10,.1]
# it will produce 100 points
# [1.0, 1.1, ... , 9.9, 10]
#

import matplotlib.pyplot as plt
import numpy as np

#Generar función de 1 a 10 con incremento de .1 y graficar a la vez

#rango de eje x
x = np.arange(0,10,1)

#rango de eje y
y = [Xn for Xn in x]

#configurar grafica con color verde
plt.scatter(x,y,color="green")

#graficar
plt.show()
