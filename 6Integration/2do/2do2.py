#
# 2do
# segundo ejercicio
# dado (7**(-x))+3 cuando a = -1 y b = 2

def f(x):
    return (7**(-x))+3

a = -1
b = 2

#Regla del rectángulo
r1 = f(a)*(b-a)
print("El resultado es: ",r1)


#regla del punto medio
r2 = f((a+b)/2)*(b-a)
print('El resultado es: ',r2)

#regla del trapecio
r3 = ((b-a)/2)*(f(a)+f(b))
print('El resultado es: ',r3)


#regla del Simpson
r4 = ((b-a)/6)*(f(a)+(4*f((a+b)/2)+f(b)))
print('El resultado es: ',r4)