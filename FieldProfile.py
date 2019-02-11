import numpy as np
import matplotlib.pyplot as plt
import rpmClass_Stable as rpm
import seaborn as sns

sns.set_style('white')



Lattice = rpm.ASI_RPM(1,1)





X = np.linspace(-1, 1, 100)
Y = np.linspace(-1, 1, 100)

Bx, By = Lattice.dipole(m=[[0, 1], [0, -1]], r=np.meshgrid(X, Y), r0=[[0.,0.], [-0.5, 0.5]])

plt.figure(figsize=(8, 8))
U = (By**2+Bx**2)**0.5
plt.streamplot(X, Y, Bx, By, density = 5, arrowsize =0.001)
plt.margins(0, 0)
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off

plt.tick_params(
    axis='y',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    left=False,      # ticks along the bottom edge are off
    right=False,         # ticks along the top edge are off
    labelleft=False) # labels along the bottom edge are off
plt.show()




