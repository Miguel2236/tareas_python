#
# 2do
#

import pickle

with open('tuple.bin','rb') as fh:
        aTuple = pickle.load(fh) 

print(type(aTuple))
print(aTuple)

print('well done...')