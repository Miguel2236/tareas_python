import math
import matplotlib.pyplot as plt
import numpy as np

#dada e^2-x - 7x = 0

#valor de euler
e = 2.718281828

def falsaPosicion():
    #Metodo de la falsa posición

    #Ck = (f(bk)*ak - f(ak)bk)/(f(bk) - f(ak))

    #Intervalos [ak,bk]

    int = [2,4]

    #obtener f(ak) y f(bk)

    fa = (e**(2-2)) - 7*(2)

    fb = (e**(2-4)) - 7*(4)

    ck = ((fb*int[0])-(fa*int[1]))/(fb-fa)

    print("f(a) = ",fa," fb = ",fb," C = ",ck)

    #grafica

    #np.linspace(desde donde empieza en X, hasta donde llega en X, cantidad de puntos para unir)
    x = np.linspace(fa, fb, 300)
    y = (e**(2-x)) - 7*x

    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()


falsaPosicion()

