#
# select and write 
# one of the following stat functions
#

def sum(lst):
    res = 0
    for x in lst:
        res += x
        print(res)
    return res

def avg(l):
    avg = sum(l) / len(l)
    print("El promedio es: ",avg)

def min(l): pass

def max(l): pass

def range(l):
    for x in range(l):
        print(x)

def std(l): pass

def mode(l): pass


lst = [1,5,10,11,2]

sum(lst)

avg(lst)

min(lst)

#range(20)

std(lst)

mode(lst)