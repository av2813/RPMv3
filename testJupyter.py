import rpmClass_Stable as rpm
import numpy as np
import math
import os
import matplotlib.pyplot as plt
import seaborn as sns
import re
import pandas as pd
from importlib import *			#Package to update the version of rpmClass_Stable

reload(rpm)
#sns.set_style("ticks")

Lattice = rpm.ASI_RPM(10, 10)

Lattice.kagome(0.1, 0.02)

#print(Lattice.effCoerFieldList(n=3, unit_vector = [1,1,0]))
#Lattice.randomMag()

name = r'SingleSpinFlipTest1'
#Lattice.squareGroundState()
Lattice.save(r'SingleSpinFlipTest1')
Lattice.fieldSweepSingleSpin(-0.15, np.pi/4, n=5)
#Lattice.fieldSweepSingleSpin(-0.1, 0, n=5)
Lattice.load(os.path.join(os.getcwd(), r'SingleSpinFlipTest1'+'.npz'))
Lattice.fieldSweepSingleSpin(0.09, np.pi/4, n=5)