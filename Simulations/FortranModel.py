'''
Created on 5 Dec 2015

@author: s1144899
'''
import numpy as np
import simulate
w = np.ones((4,4))
Vr = 0.0*np.ones(4)
Vs = 0.0*np.ones(4)
I_c = 20.0*np.ones(4)
Vt = 15.0*np.ones(4)
Tau_Md = 10.0*np.ones(4)
dt = 0.1
en = 100
print simulate.simulate(w,Vr,I_c,Vt,Tau_Md,Vs,dt,en)
