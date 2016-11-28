'''
Created on 2 Dec 2015

@author: s1144899
'''
import numpy as np
class neuron:
    def __init__(self, V_rIN, V_thIN, tau_mIN, I_cIN,neurons):
        self.V_r = float(V_rIN)
        self.I_c = float(I_cIN)
        self.V_th = float(V_thIN)
        self.tau_mD = 1/float(tau_mIN)
        self.V = self.V_r
        self.spikeRecordT = []
        self.V_rec = []
        self.incomingSpikes = []
        self.neurons = neurons
    def update(self,dt,t,weights,i,lastSpikes,lastSpikesDiff):
        I_s = 0.0
        self.I_s = np.sum(np.multiply(weights[:,i],lastSpikesDiff))
        self.V += -(self.V-(self.I_c+I_s))*self.tau_mD*dt
        if self.V > self.V_th:
            self.V = self.V_r
            self.spikeRecordT.append(t)
            lastSpikes[i] = t
        if t-int(t)<dt:
            return#self.V_rec.append(self.V)
    def reset(self):
        self.spikeRecordT = []
        self.V = self.V_r
    def getSpikes(self):
        return self.spikeRecordT
    def getVRec(self):
        return self.V_rec
            
        