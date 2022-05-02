#
# radious of circle inscribed in a tringle
# place here your solution code
#
# capturar los lados del triangulo, a b y c
# obtener el semiperimetro s = 0.5(a + b + c)
# con el semiperimetro obtener el radio sqrt(s(s-a)*(s-b)*(s-c))
import math

a = input("Valor de a ")
b = input("Valor de b ")
c = input("Valor de c ")

try:

    a = float(a)
    b = float(b)
    c = float(c)

    #semiperimetro
    s = 0.5*(a + b + c)

    #radio
    r = (math.sqrt(s*(s-a)*(s-b)*(s-c)))/s

    print("Los valores son a = ",a," b = ",b," c = ",c)

    print("El radio es: ", r)

except:
    #si los valores son inválidos
    print("Valores invalidos")
