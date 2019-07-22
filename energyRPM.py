import rpmClass_Stable as rpm
import numpy as np
import math
import os
import matplotlib.pyplot as plt
#import seaborn as sns
import re
import pandas as pd
from importlib import *			#Package to update the version of rpmClass_Stable

reload(rpm)

#Initial testing of the energy functions

lattice = rpm.ASI_RPM(5, 5)

lattice.square()
lattice.squareGroundState()
lattice.randomMag()
#lattice.squareType3State()

#print(lattice.Elocal(5, 4, 5))
#bprint(lattice.Etotal(5))

def energyStateTest(dim, n):
    lattice = rpm.ASI_RPM(dim,dim)
    lattice.square()
    lattice.squareGroundState()
    temp,Type1Energy1 = lattice.Etotal(n)
    #lattice.vertexCharge2()
    #lattice.graphCharge()
    lattice.flipAll()
    temp,Type1Energy2 = lattice.Etotal(n)
    lattice.square()
    temp,Type2Energy1 = lattice.Etotal(n)
    #lattice.graphCharge()
    lattice.flipAll()
    temp,Type2Energy2 = lattice.Etotal(n)
    lattice.square()
    lattice.squareType3State()
    temp,Type3Energy1 = lattice.Etotal(n)
    #lattice.graphCharge()
    lattice.flipAll()
    temp,Type3Energy2 = lattice.Etotal(n)
    lattice.square()
    lattice.squareMonopoleState()
    temp,Type4Energy1 = lattice.Etotal(n)
    #lattice.graphCharge()
    lattice.flipAll()
    temp,Type4Energy2 = lattice.Etotal(n)
    return([dim, n, Type1Energy1,Type1Energy2,Type2Energy1,Type2Energy2,Type3Energy1,\
           Type3Energy2,Type4Energy1,Type4Energy2])
    #return({'Type1Energy1':Type1Energy1, \
	#	'Type1Energy2':Type1Energy2, \
	#	'Type2Energy1':Type2Energy1, \
	#	'Type2Energy2':Type2Energy2, \
	#	'Type3Energy1':Type3Energy1, \
	#	'Type3Energy2':Type3Energy2, \
	#	'Type4Energy1':Type4Energy1, \
	#	'Type4Energy2':Type4Energy2})
'''
energy_steps = []
for n in np.arange(1, 10, 1):
    energy_steps.append(energyStateTest(10, n))

folder = os.getcwd()
file = 'EnergyTest.txt'
np.savetxt(os.path.join(folder, file), energy_steps)
'''

energy_steps = []
for n in [5,6,7,8,9,10,12,14,16,18,20, 25, 30, 50, 100]:
    energy_steps.append(energyStateTest(n, 6))
folder = os.getcwd()
file = 'EnergyTest2.txt'
np.savetxt(os.path.join(folder, file), energy_steps)
#print(energyStateTest(10, 1))
#print(energyStateTest(10, 2))
#print(energyStateTest(10, 3))
#print(energyStateTest(10, 4))
#print(energyStateTest(10, 5))
#print(energyStateTest(10, 6))
#print(energyStateTest(10, 7))
#print(energyStateTest(10, 8))
#print(energyStateTest(10, 9))
