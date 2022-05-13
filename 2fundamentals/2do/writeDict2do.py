#
# 2do
#

import pickle

d={'one':'aaa aaa', 'two':'bbb bbb', 'three':'ccc ccc', 'four':'XYZ'}

with open('dict.bin','wb') as fh:
        pickle.dump(d,fh)

print('well done...')