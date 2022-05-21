#
# select and write 
# one of the following stat functions
#
import numpy

import statistics as stats

def sum(lst):
    res = 0
    for x in lst:
        res += x
        print(res)
    return res

def avg(l):
    avg = sum(l) / len(l)
    print("El promedio es: ",avg)

def minimo(l):
    x = min(l)
    print(x)


def maximo(l):
    print (max(l))

def rango():
    x = range(3,10)
    for n in x:
        print(n)

def std(l):
    stand = numpy.std(l)
    print(stand)

def mode(l):
    x = stats.mode(l)
    print("mode es: ",x)


lst = [1,5,10,11,2]

sum(lst)

avg(lst)

minimo(lst)

maximo(lst)

rango()

std(lst)

mode(lst)