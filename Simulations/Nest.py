'''
Created on 3 Dec 2015

@author: s1144899
'''
import nest
import pylab
import numpy as np
from datetime import datetime
def build_network(dt) :

    nest.ResetKernel()
    nest.SetKernelStatus({"local_num_threads" : 1, "resolution" : dt})
    for i in range(24):
        neuron = nest.Create('iaf_neuron')
        nest.SetStatus(neuron, "I_e", 376.0)
        vm = nest.Create('voltmeter')
        nest.SetStatus(vm, "withtime", True)
        sd = nest.Create('spike_detector')
        nest.Connect(vm, neuron)
        nest.Connect(neuron, sd)
    return vm, sd
dt = 0.001
print("Running simulation with dt=%.2f" % dt)
vm, sd = build_network(dt)
a = datetime.now()
nest.Simulate(100000.0)
b = datetime.now()
print b-a