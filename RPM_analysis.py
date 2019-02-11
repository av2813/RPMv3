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
from matplotlib import rcParams
from matplotlib import rc
import time
import matplotlib.cm as cm
import matplotlib
from matplotlib.colors import ListedColormap
from matplotlib.colors import LinearSegmentedColormap
reload(rpm)     #make sure that the class is updated with any changes
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rcParams.update({'figure.autolayout': True})
rc('text', usetex=True)
#sns.set_context('poster')

sns.set_style('ticks')
savefolder = r'C:\Users\av2813\Box\GitHub\RPM\RPM_Data\PeriodDoublingFigures\ZurichPoster'
name = 'Square1p_Test'
#
#sns.set_palette("dark", 3)
sns.palplot(sns.color_palette("coolwarm"))
#my_cmap = ListedColormap(sns.color_palette('coolwarm').as_hex())




folder = r'D:\RPM_Rapid\SquarePeriodDouble\PeriodDoublingData_QD1.000000e-01_Width4.200000e-07_Count3'  #Interesting Square Lattice
#folder = r'D:\RPM_Rapid\SquarePeriodDouble\PeriodDoublingData_QD8.000002e-02_Width2.400000e-07_Count2'  #Interesting Square Lattice
#folder = r'D:\RPM_Rapid\ShaktiPeriodDoublingv2\PeriodDoublingData_QD2.400008e-02_Width2.000000e-07_Count1'
#folder = r'D:\RPM_Rapid\TetrisPeriodDouble\PeriodDoublingData_QD7.200003e-02_Width2.400000e-07_Count1'
#folder = r'D:\RPM_Rapid\SquarePeriodDoubleRAND\PeriodDoublingData_QD7.200003e-02_Width2.800000e-07_Count3'
#file = r'FinalRPMLattice_Hmax1p414214e-01_steps10_Angle7p853982e-01_neighbours5_Loops10.npz'
#file =r'
#state_file = r'RPMStateInfo_Hmax1.414214e-01_steps10_Angle7.853982e-01_neighbours5_Loops10.npz'
#state_data= np.load(os.path.join(folder,state_file))

#folder = r'D:\RPM_Rapid\CorrelationTestFolders\Hc_std5.000000e-02'
#folder = r'D:\RPM_Rapid\CorrelationTestFolders\Hc_std2.000000e-02'

# def correlationGraph(folders):
#     data = []
#     for folder in folders:
#         fieldStr = []
#         field = []
#         mag = []
#         monopole = []
#         correlatin = []
#         for root, subpath, files in os.walk(folder):
#             new_files = list(filter(lambda x: 'Lattice_counter' in x, files))
#             new_files.sort(key = sortFunc)
#             for file in new_files:
#                 if 'Lattice_counter' in file:
#                     Lattice.load(os.path.join(root, file))
#                     #print(file[file.find('_Angle')+6:file.find('.npz')])
#                     angle = float(file[file.find('_Angle')+6:file.find('.npz')].replace('p', '.'))
#                     Happlied = float(file[file.find('Applied')+7:file.find('_Angle')].replace('p', '.'))
#                     fieldStr.append(Happlied)
#                     field.append(np.array([Happlied*np.cos(angle), Happlied*np.sin(angle)]))
#                     magnew = Lattice.netMagnetisation()
#                     mag.append(magnew[0]+magnew[1])
#                     monopole.append(Lattice.monopoleDensity())
#                     correlation.append(1)
#                     if sortFunc(file) >24:
#                         Lattice.correlation(Lattice, Lattice.load())
#                     if sortFunc(file) == 202:
#                         Happlied = 0
#                         fieldStr.append(Happlied)
#                         field.append(np.array([Happlied*np.cos(angle), Happlied*np.sin(angle)]))
#                         magnew = Lattice.netMagnetisation()
#                         mag.append(magnew[0]+magnew[1])
#                         monopole.append(Lattice.monopoleDensity())
#         data.append([fieldStr, field, mag, monopole])
#     return(data)
def forceAspect(ax,aspect=1):
    im = ax.get_images()
    extent =  im[0].get_extent()
    ax.set_aspect(abs((extent[1]-extent[0])/(extent[3]-extent[2]))/aspect)


Lattice = rpm.ASI_RPM(1,1)
sns.set_context('poster', font_scale = 2)
corr_list = Lattice.correlationAll(folder)
#plt.savefig(os.path.join(savefolder, name+'Progress.svg'), transparent=True)
#plt.savefig(os.path.join(savefolder, name+'Progress.png'), transparent=True)
sns.set_style('ticks')
sns.set_style({'axes.grid':True})
fig, ax = plt.subplots(1, 1)
plt.plot(corr_list[:125])
plt.ylabel('Correlation')
plt.xlabel('Minor Loop')
xticks = np.array([11, 36, 61, 86, 111, 136])
ax.set_xticks(xticks)
ax.set_xticklabels([r'2', r'3', r'4', r'5', r'6'])
#ax.set(adjustable='box-forced', aspect='equal')
#plt.axhline(y=1., color = 'k')
#plt.savefig(os.path.join(savefolder, name+'Corrv2.svg'), transparent=True)
plt.savefig(os.path.join(savefolder, name+'Corrv2.png'), transparent=True)

plt.show()
Lattice.fieldSweepAnalysis(folder)
Lattice.load(os.path.join(folder, file))
Lattice.graph()
Lattice.localPlot(28,40, 10)

#Lattice.fieldSweepAnimation(folder)#plt.show()
def display_cmap(cmap):
    plt.imshow(np.linspace(0, 100, 256)[None, :],  aspect=25,    interpolation='nearest', cmap=cmap) 
    plt.axis('off')
cdict1 = {'red':   ((0.0, 0.0, 0.0),
                   (0.5, 0.0, 0.1),
                   (1.0, 1.0, 1.0)),

         'green': ((0.0, 0.0, 0.0),
                   (1.0, 0.0, 0.0)),

         'blue':  ((0.0, 0.0, 1.0),
                   (0.5, 0.1, 0.0),
                   (1.0, 0.0, 0.0))
        }
#blue_red1 = LinearSegmentedColormap('BlueRed1', cdict1)

#display_cmap(blue_red1)
#plt.show()

test = matplotlib.markers.MarkerStyle(marker='o', fillstyle=None)
def graph(ax, lattice, unit_cell_len=None, lattice_prev=None, name = ''):
    '''
    Plots the positions and directions of the bar magnetisations as a quiver graph
    '''
    x = 24
    y = 21
    n = 11
    x1 = x - n
    x2 = x + n+1
    y1 = y - n
    y2 = y + n+1
    if lattice_prev == None:
        print('dont care')
    else:
        count_diff = lattice[:, :, 7] - lattice_prev[:,:,7]
        #count_diff = count_diff
        #count_diff[np.where(count_diff>1.5)] = 0
        print(count_diff)
        #local_cd = count_diff[x1:x2,y1:y2]
        count_diff = count_diff.flatten()

    grid = lattice

    
    
    # if x1<0:
    #     x1 = 0
    # if x2>side_len_x:
    #     x2 = side_len_x -1
    # if y1<0:
    #     y1 = 0
    # if y2>side_len_y-1:
    #     y2 = side_len_y-1

    local = grid[x1:x2,y1:y2,:]
    
    X = grid[:,:,0].flatten()
    Y = grid[:,:,1].flatten()
    z = grid[:,:,2].flatten()
    Mx = grid[:,:,3].flatten()
    My = grid[:,:,4].flatten()
    Mz = grid[:,:,5].flatten()
    Hc = grid[:,:,6].flatten()
    X[np.where(Hc==0)] = -1
    Y[np.where(Hc==0)] = -1
    C = grid[:,:,7].flatten()
    Charge = grid[:,:,8].flatten()
    Hc[np.where(Hc == 0)] = np.nan

    #sns.palplot(sns.color_palette("dark", 3))
    #plt.show()
    #plt.set_cmap(sns.color_palette("dark", 3))
    #plt.set_cmap('RdBu')

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
    #fig, ax = plt.subplots(figsize = fig_size)
    #plt.set_cmap('coolwarm')
    if lattice_prev == None:
        plt.set_cmap('coolwarm')
        graph = ax.quiver(X, Y, Mx, My, width = 0.009,headlength =4, minshaft = 2,minlength = 3, angles='uv', scale_units='xy', pivot = 'mid')  
        ax.set_xlim([x1 - unit_cell_len, x2+unit_cell_len])
        ax.set_ylim([y1 - unit_cell_len, x2+unit_cell_len])
        #ax.set_xlim([-1*unit_cell_len+np.min(X), np.max(X)+unit_cell_len])
        #ax.set_ylim([-1*unit_cell_len+np.min(X), np.max(Y)+unit_cell_len])
    else:
        plt.set_cmap('viridis')
        #cmap.set_under(color = 'k')
        graph = ax.scatter(X, Y, s = 100., c=count_diff, marker =None, linewidth=0.1)
        ax.set_xlim([x1 - unit_cell_len, x2+unit_cell_len])
        ax.set_ylim([y1 - unit_cell_len, x2+unit_cell_len])
        #ax.set_xlim([-1*unit_cell_len+np.min(X), np.max(X)+unit_cell_len])
        #ax.set_ylim([-1*unit_cell_len+np.min(X), np.max(Y)+unit_cell_len])
        graph = ax.quiver(X, Y, Mx, My, width = 0.009,headlength =4, minshaft = 2,minlength = 3, angles='uv', scale_units='xy',  pivot = 'mid') 

    ax.set_xlim([-1*unit_cell_len, np.max(X)+unit_cell_len])
    ax.set_ylim([-1*unit_cell_len, np.max(X)+unit_cell_len])
    ax.set(adjustable='box-forced', aspect='equal')
    #plt.ticklabel_format(style='sci', scilimits=(0,0))
    #ax.set_title(name)
    plt.tight_layout()
    #ax.set_title('Counts')
    return(ax)


#def 
ans = float(Lattice.returnUnitCellLen())



filename = []
for root, sub, files in os.walk(folder):
    for file in files:
        if '1p414214e-01_Angle' in file:
            filename.append(file)
i=0
print(i)
print(filename)
print(len(filename))
def sortFunc(element):
    #print(element)
    begin = element.find('counter')+7
    end = element.find('_Loop')
    #print(element.find('counter'))
    #print(element.find('_Loop'))
    #print(int(element[begin:end]))
    return(int(element[begin:end]))

filename.sort(key = sortFunc)
print(filename)
Lattice_list = []
filename = filename[:14]
sns.set_style('white')
fig, ax = plt.subplots(2, int(len(filename)/2))
savetemp = r'D:\RPM_Rapid\Hysteresis\PeriodDoubleFigures'
namePD = r'4MicroState'
for file in filename:
    fig, ax = plt.subplots(1,1)
    Lattice.load(os.path.join(folder, file))
    Lattice_list.append(Lattice.returnLattice())
    if i>=2:
        ax = graph(ax,Lattice.returnLattice(), unit_cell_len = ans, lattice_prev = Lattice_list[i-2], name=str(i))
    elif i==1:
        ax = graph(ax,Lattice.returnLattice(), unit_cell_len = ans, name=str(i))
    else:
        ax = graph(ax,Lattice.returnLattice(), unit_cell_len = ans, name=str(i))
    i+=1
    plt.savefig(os.path.join(savetemp, namePD+'%(i)d.svg' % locals()), transparent=True)
    plt.savefig(os.path.join(savetemp, namePD+'%(i)d.png' % locals()), transparent=True)
    plt.show()
#print(ax.flatten())
#ax = np.transpose(ax)
for axes in ax.flatten():
    print(i, axes, filename[i])
    axes.set(adjustable='box-forced', aspect='equal')
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    Lattice.load(os.path.join(folder, filename[i]))
    Lattice_list.append(Lattice.returnLattice())
    print(Lattice_list)

    if i>=2:
        axes = graph(axes,Lattice.returnLattice(), unit_cell_len = ans, lattice_prev = Lattice_list[i-2], name=str(i))
    elif i==1:
        axes = graph(axes,Lattice.returnLattice(), unit_cell_len = ans, lattice_prev = Lattice_list[i], name=str(i))
    else:
        axes = graph(axes,Lattice.returnLattice(), unit_cell_len = ans, lattice_prev = Lattice_list[i], name=str(i))
    i+=1


plt.savefig(os.path.join(savefolder, name+'Percentage.svg'), transparent=True)
plt.savefig(os.path.join(savefolder, name+'Percentage.png'), transparent=True)
plt.show()
j=0
plt.set_cmap('Blues')
for Lat in Lattice_list:
    if j ==0:
        testLat = Lat
        testLat[:,:,8] = np.absolute(testLat[:,:,8])
        new_lattice =testLat
    else:
        new_lattice[:,:,8] =  np.add(new_lattice[:,:,8], abs(Lat[:,:,8]))
    j+=1

new_lattice[:,:,8] = new_lattice[:,:, 8]/len(Lattice_list)

sumLattice = rpm.ASI_RPM(20, 20, lattice = new_lattice)
print(sumLattice.returnLattice())
sumLattice.graphCharge()


# file = r'Lattice_counter11_Loop0_FieldApplied1p414214e-01_Angle7p853982e-01.npz'
# Lattice.load(os.path.join(folder, file))
# ax[0,0] = graph(ax[0,0],Lattice.returnLattice(), unit_cell_len = ans)
# #ax[0,0].set_ylabel(r'$\mu m$')
# #plt.setp(ax[0,0].get_xticklabels(), visible=False)
# file = r'Lattice_counter23_Loop0_FieldApplied-1p414214e-01_Angle7p853982e-01.npz'
# Lattice.load(os.path.join(folder, file))
# ax[0,1] = graph(ax[0,1],Lattice.returnLattice(), unit_cell_len = ans)
# #plt.setp(ax[0,1].get_xticklabels(), visible=False)
# #plt.setp(ax[0,1].get_yticklabels(), visible=False)
# file = r'Lattice_counter36_Loop1_FieldApplied1p414214e-01_Angle7p853982e-01.npz'
# Lattice.load(os.path.join(folder, file))
# ax[1,0] = graph(ax[1,0],Lattice.returnLattice(), unit_cell_len = ans)
# #ax[1,0].set_xlabel(r'$\mu m$')
# #ax[1,0].set_ylabel(r'$\mu m$')
# file = r'Lattice_counter48_Loop1_FieldApplied-1p414214e-01_Angle7p853982e-01.npz'
# Lattice.load(os.path.join(folder, file))
# ax[1,1] = graph(ax[1,1],Lattice.returnLattice(), unit_cell_len = ans)
# #ax[1,1].set_xlabel(r'$\mu m$')



#plt.setp(ax[1,1].get_yticklabels(), visible=False)




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