import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
import rpmClass_Stable as rpm
import os
from matplotlib import rcParams
import pandas as pd

from importlib import *			#Package to update the version of rpmClass_Stable

reload(rpm)

#sns.set_style('ticks')

Hc = 0.018
Hc_std = 0.05
width = 120e-9
thickness = 14e-9
length = 400e-9
gap = 100e-9
magnetisation = 800e3
dimensions = 10

lattice = rpm.ASI_RPM(dimensions,dimensions, bar_length = length, \
					vertex_gap = gap, bar_thickness = thickness, \
        			bar_width = width, magnetisation = magnetisation)

lattice.square(Hc, Hc_std)
folder = 
file = 
filename = os.path.join()
lattice.load()

#lattice.graphState()
#lattice.squareGroundState()

#lattice.hysteresisCumulative(5)
#lattice.flipAll()
#lattice.flipSpin(20, 21)
lattice.effectiveCoerciveCumulative(n=5)
#print(lattice.effectiveCoerciveHistogram(n= 5))
lattice.vertexCharge2()
#print(lattice.returnLattice()[:,:,8])
#fig = plt.figure(figsize=(9, 9))
#ax = fig.add_subplot(111)
#ax = lattice.graphSpins(ax, lattice.returnLattice())
#plt.show()
field = np.array([-0.017, -0.017,0])
lattice.relax(field, n= 5)
field = np.array([-0.0178, -0.0178,0])
lattice.relax(field, n= 5)
field = np.array([-0.01785, -0.01785,0])
lattice.relax(field, n= 5)

lattice.vertexCharge2()
#print(lattice.returnLattice()[:,:,8])
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)
ax = lattice.graphSpins(ax, lattice.returnLattice())
plt.show()