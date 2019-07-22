import numpy as np
import matplotlib.pyplot as plt
import rpmClass_Stable as rpm
import seaborn as sns

sns.set_style('white')



Lattice = rpm.ASI_RPM(5,5)

Lattice.square()
Lattice.randomMag()
Lattice.fieldProfile(100, density = 20)