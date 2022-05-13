import math

#dado (-1,3),(0,-7),(4,7),(5,11) calcular con lagrange

p1 = [-1,3]
p2 = [0,-7]
p3 = [4,7]
p4 = [5,11]

#Declarar el valro de X
x = 3.2
def calcular():

    #primera iteración
    x1 = ((x - p2[0]) / (p1[0] - p2[0]))
    x2 = ((x - p3[0]) / (p1[0] - p3[0]))
    x3 = ((x - p4[0]) / (p1[0] - p4[0]))
    aRes01 = x1 * x2 * x3 * p1[1]

    #segunda iteración
    x4 = ((x - p1[0]) / (p2[0] - p1[0]))
    x5 = ((x - p3[0]) / (p2[0] - p3[0]))
    x6 = ((x - p4[0]) / (p2[0] - p4[0]))
    aRes02 = x4 * x5 * x6 * p2[1]

    #tercera iteración
    x7 = ((x - p1[0]) / (p3[0] - p1[0]))
    x8 = ((x - p2[0]) / (p3[0] - p2[0]))
    x9 = ((x - p4[0]) / (p3[0] - p4[0]))
    aRes03 = x7 * x8 * x9 * p3[1]

    #cuarta iteración
    x10 = ((x - p1[0]) / (p4[0] - p1[0]))
    x11 = ((x - p2[0]) / (p4[0] - p2[0]))
    x12 = ((x - p3[0]) / (p4[0] - p3[0]))
    aRes04 = x10 * x11 * x12 * p4[1]

    y = aRes01 + aRes02 + aRes03 + aRes04

    print("El valor de X es: ",x,", el valor de Y es: ",y)

calcular()