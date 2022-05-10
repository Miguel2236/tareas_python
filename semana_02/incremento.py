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