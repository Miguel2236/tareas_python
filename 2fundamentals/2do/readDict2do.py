#
# 2do
#

import pickle

with open('dict.bin','rb') as fh:
        aDict = pickle.load(fh) 

print(type(aDict))
print(aDict)

print('well done...')