import numpy as np
import os
import matplotlib.pyplot as plt
#import seaborn as sns
import scipy.optimize as sco
from pathlib import Path
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FormatStrFormatter
import rpmClass_Stable as rpm
from importlib import *

reload(rpm)		#make sure that the class is updated with any changes


folder = r'D:\RPM_Rapid\ShaktiPeriodDoublingv2\PeriodDoublingData_QD7.600002e-02_Width2.400000e-07_Count3'
file = r'FinalRPMLattice_Hmax1p414214e-01_steps10_Angle7p853982e-01_neighbours5_Loops10.npz'
#file =r'

Lattice = rpm.ASI_RPM(1,1)
Lattice.load(os.path.join(folder, file))
#Lattice.graph()
#Lattice.localPlot(28,40, 10)

#Lattice.fieldSweepAnimation(folder)
#plt.show()

def graph(ax, lattice,fig_size = (2,10), unit_cell_len=None):
    '''
    Plots the positions and directions of the bar magnetisations as a quiver graph
    '''
    grid = lattice
    X = grid[:,:,0].flatten()
    Y = grid[:,:,1].flatten()
    z = grid[:,:,2].flatten()
    Mx = grid[:,:,3].flatten()
    My = grid[:,:,4].flatten()
    Mz = grid[:,:,5].flatten()
    Hc = grid[:,:,6].flatten()
    C = grid[:,:,7].flatten()
    Charge = grid[:,:,8].flatten()
    Hc[np.where(Hc == 0)] = np.nan
    #fig, ax = plt.subplots(figsize = fig_size)
    #plt.set_cmap(cm.plasma)
    graph = ax.quiver(X, Y, Mx, My, C, angles='uv', scale_units='xy',  pivot = 'mid')     #
    ax.set_xlim([-1*unit_cell_len, np.max(X)+unit_cell_len])
    ax.set_ylim([-1*unit_cell_len, np.max(X)+unit_cell_len])
    ax.set_title('Counts')
    return(ax)
ans = float(Lattice.returnUnitCellLen())

fig, ax = plt.subplots(10,2)
file = r'Lattice_counter11_Loop0_FieldApplied1p414214e-01_Angle7p853982e-01.npz'
Lattice.load(os.path.join(folder, file))
print(np.shape(ax))
ax[0,0] = graph(ax[0,0],Lattice.returnLattice(), unit_cell_len = ans)
file = r'Lattice_counter23_Loop0_FieldApplied-1p414214e-01_Angle7p853982e-01.npz'
Lattice.load(os.path.join(folder, file))
ax[1,0] = graph(ax[1,0],Lattice.returnLattice(), unit_cell_len = ans)
file = r'Lattice_counter36_Loop1_FieldApplied1p414214e-01_Angle7p853982e-01.npz'
Lattice.load(os.path.join(folder, file))
ax[0,1] = graph(ax[0,1],Lattice.returnLattice(), unit_cell_len = ans)
file = r'Lattice_counter48_Loop1_FieldApplied-1p414214e-01_Angle7p853982e-01.npz'
Lattice.load(os.path.join(folder, file))
ax[1,1] = graph(ax[1,1],Lattice.returnLattice(), unit_cell_len = ans)

file = r'Lattice_counter36_Loop1_FieldApplied1p414214e-01_Angle7p853982e-01.npz'
Lattice.load(os.path.join(folder, file))
ax[0,1] = graph(ax[0,1],Lattice.returnLattice(), unit_cell_len = ans)
file = r'Lattice_counter48_Loop1_FieldApplied-1p414214e-01_Angle7p853982e-01.npz'
Lattice.load(os.path.join(folder, file))
ax[1,1] = graph(ax[1,1],Lattice.returnLattice(), unit_cell_len = ans)

file = r'Lattice_counter36_Loop1_FieldApplied1p414214e-01_Angle7p853982e-01.npz'
Lattice.load(os.path.join(folder, file))
ax[0,1] = graph(ax[0,1],Lattice.returnLattice(), unit_cell_len = ans)
file = r'Lattice_counter48_Loop1_FieldApplied-1p414214e-01_Angle7p853982e-01.npz'
Lattice.load(os.path.join(folder, file))
ax[1,1] = graph(ax[1,1],Lattice.returnLattice(), unit_cell_len = ans)

file = r'Lattice_counter36_Loop1_FieldApplied1p414214e-01_Angle7p853982e-01.npz'
Lattice.load(os.path.join(folder, file))
ax[0,1] = graph(ax[0,1],Lattice.returnLattice(), unit_cell_len = ans)
file = r'Lattice_counter48_Loop1_FieldApplied-1p414214e-01_Angle7p853982e-01.npz'
Lattice.load(os.path.join(folder, file))
ax[1,1] = graph(ax[1,1],Lattice.returnLattice(), unit_cell_len = ans)

file = r'Lattice_counter36_Loop1_FieldApplied1p414214e-01_Angle7p853982e-01.npz'
Lattice.load(os.path.join(folder, file))
ax[0,1] = graph(ax[0,1],Lattice.returnLattice(), unit_cell_len = ans)
file = r'Lattice_counter48_Loop1_FieldApplied-1p414214e-01_Angle7p853982e-01.npz'
Lattice.load(os.path.join(folder, file))
ax[1,1] = graph(ax[1,1],Lattice.returnLattice(), unit_cell_len = ans)

file = r'Lattice_counter36_Loop1_FieldApplied1p414214e-01_Angle7p853982e-01.npz'
Lattice.load(os.path.join(folder, file))
ax[0,1] = graph(ax[0,1],Lattice.returnLattice(), unit_cell_len = ans)
file = r'Lattice_counter48_Loop1_FieldApplied-1p414214e-01_Angle7p853982e-01.npz'
Lattice.load(os.path.join(folder, file))
ax[1,1] = graph(ax[1,1],Lattice.returnLattice(), unit_cell_len = ans)

plt.show()

def sortFunc(element):
	print(element)
	begin = element.find('counter')+7
	end = element.find('_Loop')
	print(element.find('counter'))
	print(element.find('_Loop'))
	print(int(element[begin:end]))
	return(int(element[begin:end]))
#print(os.walk(folder))


'''
for root, sub, files in os.walk(folder):
	sortFunc(files[10])
	print(files)
	new_files = list(filter(lambda x: 'Lattice_counter' in x, files))
	new_files.sort(key = sortFunc)
	for file in new_files:
		Lattice.load(os.path.join(root, file))
		Lattice.localPlot(28,40, 10)w

'''

'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
t = np.arange(0.0, 1.0, 0.001)
a0 = 5
f0 = 3
delta_f = 5.0
s = a0*np.sin(2*np.pi*f0*t)
l, = plt.plot(t, s, lw=2, color='red')
plt.axis([0, 1, -10, 10])

axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0)
samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)


def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw_idle()
sfreq.on_changed(update)
samp.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)

rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)


def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()
radio.on_clicked(colorfunc)

plt.show()
'''