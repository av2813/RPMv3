import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
import pandas as pd
import scipy.interpolate as spi

sns.set_style('ticks')

folder = r'C:\Users\av2813\Documents\GitHub\RPMv3\testFORC3'
file = r'RPMStateInfo_Hmax1.500000e-01_steps50_Angle7.853982e-01_neighbours4.npz'
filename = os.path.join(folder, file)
npzinfo = np.load(filename)

print(npzinfo['arr_1'])
print(npzinfo['arr_3'])
field = npzinfo['arr_1']
field_rem = field[:,0]*-1*np.cos(np.pi/4)
field_app = field[:,1]
mag = npzinfo['arr_3']
magstren = mag[:,0]+mag[:,1]

print([field_rem.min(), field_rem.max()], [field_app.min(), field_app.max()])
Hint = (field_rem + field_app)/2**0.5
Hcoer = (field_app - field_rem)/2**0.5
print(field, field_rem, field_app,mag, magstren)

FORCarray = np.array([field_rem, field_app, Hcoer, Hint, magstren])
newarray = FORCarray.T.reshape((50, 50, 5))
print(FORCarray)

plt.figure()
plt.imshow(newarray[:,:,4])
#plt.show()

def partialDiv(Func_array):
	partdiv = np.zeros((50, 50, 6))
	for i in np.arange(1, 49):
		for j in np.arange(1, 49):
			partdiv[i,j, 2] = (Func_array[i+1, j+1, 4] - Func_array[i-1, j+1, 4] - Func_array[i+1, j-1, 4] + Func_array[i-1, j-1, 4])/((Func_array[i-1, j, 0]-Func_array[i+1, j, 0])*(Func_array[i, j-1, 1]-Func_array[i, j+1, 1]))
			partdiv[i,j,0:2] = Func_array[i, j, 0:2]
			partdiv[i,j, 5] = (Func_array[i+1, j+1, 4] - Func_array[i-1, j+1, 4] - Func_array[i+1, j-1, 4] + Func_array[i-1, j-1, 4])/((Func_array[i-1, j, 2]-Func_array[i+1, j, 2])*(Func_array[i, j-1, 3]-Func_array[i, j+1, 3]))
			partdiv[i,j,3:5] = Func_array[i, j, 2:4]
			print(Func_array[i, j, :], partdiv[i, j, :])
	return(partdiv)
Hint = (field_rem + field_app)/2**0.5
partdiv = partialDiv(newarray)



def func(x, y):
     return x*(1-x)*np.cos(4*np.pi*x) * np.sin(4*np.pi*y**2)**2


grid_x, grid_y = np.mgrid[0:1:100j, 0:1:200j]



points = np.random.rand(1000, 2)
values = func(points[:,0], points[:,1])



from scipy.interpolate import griddata
grid_z0 = griddata(points, values, (grid_x, grid_y), method='nearest')
grid_z1 = griddata(points, values, (grid_x, grid_y), method='linear')
grid_z2 = griddata(points, values, (grid_x, grid_y), method='cubic')

print(np.shape(grid_z0), np.shape(grid_z1), np.shape(grid_z2))

plt.subplot(221)
plt.imshow(func(grid_x, grid_y).T, extent=(0,1,0,1), origin='lower')
plt.plot(points[:,0], points[:,1], 'k.', ms=1)
plt.title('Original')
plt.subplot(222)
plt.imshow(grid_z0.T, extent=(0,1,0,1), origin='lower')
plt.title('Nearest')
plt.subplot(223)
plt.imshow(grid_z1.T, extent=(0,1,0,1), origin='lower')
plt.title('Linear')
plt.subplot(224)
plt.imshow(grid_z2.T, extent=(0,1,0,1), origin='lower')
plt.title('Cubic')
plt.gcf().set_size_inches(6, 6)
#plt.show()





steps = 500
N_rows, N_cols,test = partdiv.shape
signal = partdiv[:,:, 5]
fieldint_flat = partdiv[:,:,4].flatten()
fieldint_inter = np.linspace(Hint.min(), Hint.max(), steps)
fieldcoer_flat = partdiv[:,:,3].flatten()
fieldcoer_inter = np.linspace(Hcoer.min(), Hcoer.max(), steps)
print(np.shape(signal))
print(np.shape(partdiv[:,0,4]), np.shape(partdiv[:,0,3]))
points = np.random.rand(1000, 2)
points2 = np.reshape(partdiv[:,:,3:5].flatten(), (-1, 2))
print(np.shape(points2.T))
print([fieldcoer_flat.min(),fieldcoer_flat.max()], [fieldint_flat.min(),fieldint_flat.max()])
signal2 = signal.flatten()
print(np.shape(points2), np.shape(signal2))
grid_x, grid_y = np.meshgrid(np.linspace(fieldcoer_flat.min(),fieldcoer_flat.max(),steps), np.linspace(fieldint_flat.min(),fieldint_flat.max(),steps))
print(np.shape(grid_x), np.shape(grid_y))
interarray = spi.griddata(points2, signal2,(grid_x, grid_y), method='nearest')
extent=[Hcoer.min(),Hcoer.max(),Hint.min(),Hint.max()]
extent = np.array(extent)*100
test2 = np.nan_to_num(interarray)
print(interarray, np.shape(test2))
plt.figure()
plt.imshow(test2.T, origin='lower', extent=np.array(extent), cmap = 'afmhot')
plt.xlabel('Coercive field (mT)')
plt.ylabel('Interaction field (mT)')
#plt.xticks(np.linspace(Hcoer.min(),Hcoer.max(),1000))
#plt.yticks(np.linspace(Hint.min(),Hint.max(),1000))
plt.show()



interFunc = spi.RegularGridInterpolator((partdiv[:,0,3], partdiv[0,:,4]), abs(signal))
xy = np.mgrid[fieldcoer_inter, fieldint_inter].reshape(2,-1).T
fieldsize, = np.shape(fieldint_inter)
sig_inter = interFunc(xy).reshape(-1, fieldsize)
print(np.where(sig_inter == np.nan))
sig_inter[np.where(sig_inter == np.nan)] = 0

fig, ax = plt.subplots(1,1)
ax.imshow(sig_inter, origin = 'lower', cmap = 'afmhot')
ax.set_xlabel('Coercive field (mT)')
ax.set_ylabel('Interaction field (mT)')
plt.tight_layout()
plt.show()

fmr_signal = df_FMR['IQ'].as_matrix()
fmr_sig2 = np.transpose(np.reshape(fmr_signal, (N_rows, -1)))
field_array = df_settings['Field(Oe)'].as_matrix()
freq_start = df_settings['Freq Start (GHz)'].mean()
freq_stop = df_settings['Freq Stop (GHz)'].mean()
freq_step = df_settings['Freq Step (GHz)'].mean()
print(freq_start, freq_stop, freq_step)
freq_array = np.arange(freq_start, freq_stop+freq_step, freq_step)
print(np.shape(freq_array))
interFunc = spi.RegularGridInterpolator((freq_array, field_array), fmr_sig2)
xy = np.mgrid[freq_start:freq_stop:freq_int, -1000:1000:field_int].reshape(2,-1).T
freq_inter = np.arange(2, 16, freq_int)
field_inter = np.arange(-1000, 1000, field_int)
fieldsize, = np.shape(field_inter)
freqsize, = np.shape(freq_inter)
print(np.shape(xy), 2800*2000)
FMRsig_inter = interFunc(xy).reshape(-1, fieldsize)

plt.figure()
plt.imshow(partdiv[:,:,5], origin = 'lower', cmap = 'afmhot')
plt.show()

x = partdiv[:,:,3].flatten()
y = partdiv[:,:,4].flatten()
z = partdiv[:,:,5].flatten()
print(x, y, z)
df = pd.DataFrame.from_dict(np.array([x,y,z]).T)
df.columns = ['X_value','Y_value','Z_value']
df['Z_value'] = pd.to_numeric(df['Z_value'])
print(df)
pivotted= df.pivot('Y_value','X_value','Z_value')
plt.figure()
sns.heatmap(pivotted,cmap='RdBu')
plt.show()