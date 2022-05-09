import math

# Dado (-2,4), (-1,-2), (3,5), (4.3,11) encontrar (7.7,y)

# determinar b1, b2 y b3 usando interpolacion de newton

y = '';

p1 = [-2,4]
p2 = [-1,-2]
p3 = [3,5]
p4 = [4.3,11]
p5 = [7.7]

def calcular(p1,p2,p3,p4,p5):

    eMsg = ''

    #b1 = (y1 - y0)/(x1 - x0)

    b1 = (p2[1] - p1[1])/(p2[0] - p1[0])

    #b2 = (((y2 - y1)/(x2 - x1)) - b1)/(x2 - x0)

    b2 = (((p3[1] - p2[1])/(p3[0] - p2[0])) - b1)/(p3[0] - p1[0])

    #b3 = ((((y3 - y2)/(x3 - x2) - (y2 -y1)/(x2 - x1))/(x3 - x1)) - b2) / (x3 - x0)

    b3 = ((((p4[1] -p3[1])/(p4[0] - p3[0]) - (p3[1] - p2[1])/(p3[0] - p2[0]))/(p4[0] - p2[0])) - b2) / (p4[0] - p1[0])

    #y = y0 + b1*(x - x0) + b2*(x - x0)*(x - x1) + b3*(x - x0)*(x - x1)*(x - x2)

    y = p1[1] + b1*(p5[0] - p1[0]) + b2*(p5[0] - p1[0])*(p5[0] - p2[0]) + b3*(p5[0] - p1[0])*(p5[0] - p2[0])*(p5[0] - p3[0])

    eMsg = "b1 = ",b1, ", b2 =",b2, ", b3 =",b3,", y = ",y

    return eMsg


print(calcular(p1,p2,p3,p4,p5))