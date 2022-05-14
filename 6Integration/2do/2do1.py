#
# 2do
# Primer ejercicio
# dado 2sen(sqrt(x))-x cuando a = 0 y b = 1.9724

from math import sin
from math import sqrt

def f(x):
    return 2*sin(sqrt(x))-x

a = 0
b = 1.9724

#Regla del rectángulo
r1 = f(a)*(b-a)
print('El resultado es: ',r1)


#regla del punto medio
r2 = f((a+b)/2)*(b-a)
print('El resultado es: ',r2)


#regla del trapecio
r3 = ((b-a)/2)*(f(a)+f(b))
print('El resultado es: ',r3)


#regla de Simpson
r4 = ((b-a)/6)*(f(a)+(4*f((a+b)/2)+f(b)))
print('El resultado es: ',r4)