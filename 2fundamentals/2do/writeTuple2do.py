#
# 2do
#

import pickle

t=12,True,3.1,'aCat','eCod'

with open('tuple.bin','wb') as fh:
        pickle.dump(t,fh)

print('well done...')
