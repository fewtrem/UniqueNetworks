'''
Created on 25 Nov 2015

@author: s1144899
'''

import numpy as np
g = [3,4,2,4,3,2,4,2,1]

print np.bincount(g)[::-1]

for t in g:
    print t
    if t == 2:
        break