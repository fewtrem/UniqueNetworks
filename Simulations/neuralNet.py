'''
Created on 2 Dec 2015

@author: s1144899
'''
from datetime import datetime
import numpy as np
from neuronC import neuron

a = datetime.now()


N = [24] # number of neurons
tau_m = [10.0] # membrane time constant /ms
V_r = [0.0]  # reset potential /mV
V_th = [15.0] # threshold potential /mV
I_c = [20.0] # constant input current / mV
Tau = 10.0

TauInv =  1/Tau
NoN = 0
neurons = []
for i in range(len(N)):
    for j in range(N[i]):
        neurons.append(neuron(V_r[i], V_th[i], tau_m[i], I_c[i],neurons)) 
        NoN += 1
weights = np.ones((NoN,NoN))
#weights = np.matrix('0 1 ;0 0 ')
lastSpikes = np.zeros(NoN)
t = 0
dt = 0.001


def getTD(t):
    return t*np.exp(1-(t*TauInv))
while t<100:
    lastSpikesDiff = getTD(t-lastSpikes)
    for i in range(NoN):
        neurons[i].update(dt,t,weights,i,lastSpikes,lastSpikesDiff)
    t+=dt
b = datetime.now()
print b-a
for i in range(NoN):
    print neurons[i].getSpikes()
    print neurons[i].getVRec()
