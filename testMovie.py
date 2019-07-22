import numpy as np
import matplotlib.pyplot as plt
import os
import rpmClass_Stable as rpm
import pandas as pd
import time
import matplotlib.cm as cm
from importlib import reload
reload(rpm)

from matplotlib.animation import FuncAnimation, FFMpegWriter

# Some global variables to define the whole run
total_number_of_frames = 100
total_width_of_sine_wave = 2 * np.pi
all_x_data = np.linspace(0, total_width_of_sine_wave, total_number_of_frames)
all_y_data = np.sin(all_x_data)

start = time.time()
def animate(frame, line):
    """
    Animation function. Takes the current frame number (to select the potion of
    data to plot) and a line object to update.
    """

    # Not strictly neccessary, just so we know we are stealing these from
    # the global scope
    global all_x_data, all_y_data

    # We want up-to and _including_ the frame'th element
    current_x_data = all_x_data[: frame + 1]
    current_y_data = all_y_data[: frame + 1]

    line.set_xdata(current_x_data)
    line.set_ydata(current_y_data)

    # This comma is necessary!
    return (line,)
'''
folder = 'D:\RPM_Rapid\SquareQDvHapp2\SquarePD_QD1.000000e-01_Happ1.030000e-01_count2'
#filenames = os.listdir(folder)
filenames = []
for f in os.listdir(folder):
	if f.endswith(".npz"):
		filenames.append(os.path.join(folder, f))
filenames.sort(key=lambda s: os.path.getmtime(s))
print(filenames)
L = rpm.ASI_RPM(1,1)
L.load(filenames[0])
lattice_update = L.returnLattice()
X = lattice_update[:,:,0]
Y = lattice_update[:,:,1]
Mx = lattice_update[:,:,3]
My = lattice_update[:,:,4]

fig, ax = plt.subplots(1,1)
lattice = ax.quiver(X, Y, Mx, My,Mx+My, pivot ='mid')

LHistory = pd.read_csv(os.path.join(folder, 'LatticeHistory.csv'), header = None)
print(LHistory)
xpos_flip = [x for x in LHistory[9].values if x != -1]
ypos_flip = [x for x in LHistory[10].values if x != -1]
print(xpos_flip, ypos_flip)

'''

def animateSSF(frame, lattice1, L, xpos_flip, ypos_flip):
	xpos = xpos_flip[frame]
	ypos = ypos_flip[frame]
	#print(xpos, ypos)
	L.flipSpin(int(xpos), int(ypos))
	L.vertexCharge2()
	L_update = L.returnLattice()
	Mx = L_update[:,:,3]
	My = L_update[:,:,4]
	#Mx[np.where(L_update[:,:,6]==0)] = np.nan
	#My[np.where(L_update[:,:,6]==0)] = np.nan
	lattice1.set_UVC(Mx, My, Mx+My)

	#X = L_update[:,:,0]
	#Y = L_update[:,:,1]
	#Charge = L_update[:,:, 8].flatten()
	#print(np.shape((X, Y)))
	#lattice2.set_offsets((X, Y))
	#print
	#lattice2.set_array(Charge)
	return(lattice1)

def animateRPM(frame, lattice, filename):
	#L = rpm.ASI_RPM(1,1)
	#print(frame, filename[frame])
	L.load(filename[frame])
	lattice_update = L.returnLattice()
	Mx = lattice_update[:,:,3].flatten()
	My = lattice_update[:,:,4].flatten()
	X[np.where(Hc==0)] = -1
	#Mx[np.where(lattice_update[:,:,6]==0)] = np.nan
	#My[np.where(lattice_update[:,:,6]==0)] = np.nan
	lattice.set_UVC(Mx, My, Mx+My)
	X = lattice_update[:,:,0].flatten()
	Y = lattice_update[:,:,1].flatten()
	Charge = lattice_update[:,:, 8].flatten()
	print(np.shape(np.hstack((X, Y))))
	lattice.set_offsets(np.vstack((X, Y)))
	#print
	lattice.set_array(Charge)
	return lattice,

def estimateTime(frames):
	time_est = frames*0.11143+0.83739
	print('Estimated time to export to mp4: ',time_est/60 ,' minutes')

def animateMono(frame, monopoles, L, xpos_flip, ypos_flip):
	
	lattice_update = L.returnLattice()
	L.vertexCharge2()
	X = lattice_update[:,:,0].flatten()
	Y = lattice_update[:,:,1].flatten()
	Charge = lattice_update[:,:, 8].flatten()
	print(np.shape(np.hstack((X, Y))))
	monopoles.set_offsets(np.hstack((X, Y)))
	#print
	monopoles.set_array(Charge)
	#Mx = lattice_update[:,:,3]
	#My = lattice_update[:,:,4]
	#Mx[np.where(lattice_update[:,:,6]==0)] = np.nan
	#My[np.where(lattice_update[:,:,6]==0)] = np.nan
	#lattice.set_UVC(Mx, My, Mx+My)
	return monopoles,
'''
folder = 'D:\RPM_Rapid\SquareQDvHapp2\SquarePD_QD1.000000e-01_Happ1.030000e-01_count2'
#filenames = os.listdir(folder)
print(len(xpos_flip))
estimateTime(len(xpos_flip))
fig.tight_layout()
anim =FuncAnimation(fig, animateSSF,frames = 1, fargs=(lattice,L, xpos_flip, ypos_flip),
                               interval=40, blit=False, repeat = False) #len(folder)
writer = FFMpegWriter(fps=25, bitrate=None)
anim.save(os.path.join(folder,"out_funcanimationSSF_2.mp4"), writer = writer)
plt.close('all')
end = time.time()
print(end-start)
'''




def makeAnimation(folder):
	start = time.time()
	print('Exporting to mp4 started: ', time.localtime(start))
	#folder = 'D:\RPM_Rapid\SquareQDvHapp2\SquarePD_QD1.000000e-01_Happ1.030000e-01_count2'
	#filenames = os.listdir(folder)
	filenames = []
	for f in os.listdir(folder):
		if f.endswith(".npz"):
			filenames.append(os.path.join(folder, f))
	filenames.sort(key=lambda s: os.path.getmtime(s))
	print(filenames)
	L = rpm.ASI_RPM(1,1)
	L.load(filenames[0])
	lattice_update = L.returnLattice()
	X = lattice_update[:,:,0].flatten()
	Y = lattice_update[:,:,1].flatten()
	Mx = lattice_update[:,:,3].flatten()
	My = lattice_update[:,:,4].flatten()
	Charge = lattice_update[:,:,8].flatten()
	Hc = lattice_update[:,:,6].flatten()
	X[np.where(Hc==0)] = -1
	fig, ax = plt.subplots(1,1)
	plt.set_cmap(cm.jet)
	lattice1 = ax.quiver(X, Y, Mx, My,Mx+My, pivot ='mid', cmap ='bwr', zorder = 1)
	ax.set_xlim([-1*L.returnUCLen(), np.max(X)+L.returnUCLen()])
	ax.set_ylim([-1*L.returnUCLen(), np.max(X)+L.returnUCLen()])
	#lattice2 = ax.scatter(X, Y, s=25,c=Charge, marker = 'o', zorder=2, vmax = 1, vmin = -1, cmap = 'RdBu')
	LHistory = pd.read_csv(os.path.join(folder, 'LatticeHistory.csv'), header = None)
	#print(LHistory)
	xpos_flip = [x for x in LHistory[9].values if x != -1]
	ypos_flip = [x for x in LHistory[10].values if x != -1]
	estimateTime(len(ypos_flip))
	fig.tight_layout()
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
	    right=False,         # ticks along the top edge are offlen(xpos_flip)
	    labelleft=False) # labels along the bottom edge are offlen(xpos_flip)
	anim = FuncAnimation(fig, animateSSF,frames = len(xpos_flip), fargs=(lattice1,L, xpos_flip, ypos_flip),
	                               interval=40, blit=False, repeat = False) #len(folder)
	#anim = FuncAnimation(fig, animateMono, frames = 10, fargs = (lattice,L, xpos_flip, ypos_flip),
	#								interval = 40, blit = False, repeat = False)
	writer = FFMpegWriter(fps=25, bitrate=None)
	outfolder = r'D:\RPM_Rapid\SquareQDvHapp2\Movies'
	#D:\RPM_Rapid\SquareQDvHapp2\SquarePD_QD1.000000e-01_Happ1.000000e-01_count1
	savename = folder[28:]
	anim.save(os.path.join(outfolder,savename+".mp4"), writer = writer)
	plt.close('all')
	end = time.time()
	print('How long it took: ', end-start)
	#print(xpos_flip, ypos_flip)

makeAnimation('D:\RPM_Rapid\SquareQDvHapp2\SquarePD_QD5.000000e-02_Happ1.200000e-01_count19')
'''
testfolder = r'D:\RPM_Rapid\SquareQDvHapp2'
for directory in os.listdir(testfolder):
	if 'count2' in directory and 'Progression' not in directory:
		folder = os.path.join(testfolder,directory)
		print(folder)

		makeAnimation(folder)
'''

'''
fig.tight_layout()
anim =FuncAnimation(fig, animateRPM,frames = len(filenames), fargs=(lattice, filenames),
                               interval=1000, blit=False, repeat = False)
anim.save(os.path.join(folder,"out_funcanimation3.mp4"))
plt.close('all')
'''
'''
# Now we can do the plotting!
fig, ax = plt.subplots(1)
# Initialise our line
line, = ax.plot([0], [0])

# Have to set these otherwise we will get one ugly plot!
ax.set_xlim(0, total_width_of_sine_wave)
ax.set_ylim(-1.2, 1.2)

ax.set_xlabel("$x$")
ax.set_ylabel("$\sin(x)$")

# Make me pretty
fig.tight_layout()

animation = FuncAnimation(
    # Your Matplotlib Figure object
    fig,
    # The function that does the updating of the Figure
    animate,
    # Frame information (here just frame number)
    np.arange(total_number_of_frames),
    # Extra arguments to the animate function
    fargs=[line],
    # Frame-time in ms; i.e. for a given frame-rate x, 1000/x
    interval=1000 / 25
)

folder = os.getcwd()
animation.save(os.path.join(folder,"out_funcanimation.mp4"))
'''