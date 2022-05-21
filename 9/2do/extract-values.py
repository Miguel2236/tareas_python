#
# convert 1st variable as tuple
# convert 2nd variable as dictionary
# convert 3rd variable as list
#
#
# 
# 
import pandas as pd
iris = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv')

# Obtenemos la base
base    = iris['sepal length']

base02  = iris['sepal width']

base03  = iris['petal length']

# Convertimos a lista
lista = base.tolist()
print(lista)
print(type(lista))

# Convertimos a tupla
tupla = tuple(base02)
print(tupla)
print(type(tupla))

# Convertimos a diccionario
list = range(1,151)
dictionary = dict(zip(list,base03))
print(dictionary)
print(type(dictionary))
