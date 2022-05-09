import math

# dato (-4,-2), (1,5), calcular (x,3.7)

#formula 

#((x - x0)/(y - y0)) = ((x - x0)/(y1 - y0))


x = '';

p1 = [-4,-2];

p2 = [1,5];

p3 = [x,3.7];

""" p1 = [1.8,-4.25];

p2 = [-3.25,-5.1];

p3 = [x,1.8]; """


# aplicar la formula despejada

x = ((p2[0] - p1[0])/(p2[1] - p1[1])) * (p3[1] - p1[1]) + p1[0]

print("el valor de x es ",x)