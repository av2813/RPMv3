import numpy as np
import os
import matplotlib.pyplot as plt
import rpmClass_Stable as rpm
import re
from importlib import *         #Package to update the version of rpmClass_Stable
import seaborn as sns

reload(rpm)
sns.set_style("ticks")
sns.set_palette("colorblind")

folder = r'C:\Users\av2813\Box\GitHub\RPM\RPM_Data\squarerandomstate3\VertexGap7.400000e-08\\'
subfolder = r'Hc_std0.000000e+00'
statefile =  r'StateCode.npz'


#fileloc = os.path.join(folder+subfolder, statefile)


#test = np.load(fileloc)

#print(test['arr_0'])

testfolder = r'C:\Users\av2813\Box\GitHub\RPM\RPM_Data\QuenchedDisorder_variation\square7\Hc_std8.000000e-02\Hmax1.38592929113'
testfile = r'RPMStateInfo_Hmax1.385929e-01_steps10_Angle7.853982e-01_neighbours5_Loops5.npz'
npzfile = np.load(os.path.join(testfolder, testfile))
array_size = np.size(npzfile['arr_2'])
#plt.figure()
print(npzfile['arr_1'])
#plt.plot(np.arange(0, array_size), npzfile['arr_2'], 'o-')
#plt.plot(np.arange(0, array_size), npzfile['arr_1'][:,1], 'o-')
#plt.show()
#print(test['arr_1'])

folderloc = os.path.join(folder)
lattice = rpm.ASI_RPM(1,1)
lattice.load(os.path.join(folder, r'FinalRPMLattice_Hmax1p414214e-01_steps10_Angle7p853982e-01_neighbours4_Loops15.npz'))
lattice.graph()
#lattice.fieldSweepAnimation(folder)

lattice.load(os.path.join(folder, r'InitialRPMLattice_Hmax1p414214e-01_steps10_Angle7p853982e-01_neighbours4_Loops15.npz'))
lattice.graph()
#lattice.fieldPlot()
#lattice.structureFactor(-4*np.pi, 4*np.pi, 100)
lattice.graphCharge()
for root, dirs, files in os.walk(folder):
      for file in files:
            #lattice.load(os.path.join(root, file))
            #lattice.graph()
            #lattice.vertexTypeMap()
            print(file)
            if 'RPMStateInfo' in file:
                  test = np.load(os.path.join(root, file))
                  print(test['arr_0'])
                  print(test['arr_1'])
                  print(test['arr_2'])
                  print(test['arr_3'])
                  print(test['arr_4'])
                  print(test['arr_5'])
                  print('Hmax', test['arr_0'][0])
                  print('steps', test['arr_0'][1])
                  print('Htheta', test['arr_0'][2])
                  print('n', test['arr_0'][3])
                  print('loops', test['arr_0'][4])
                  print('Hc', test['arr_0'][5])
                  print('Hc_std', test['arr_0'][6])
                  print('Happlied', test['arr_0'][0]*np.sin(np.pi/4.))
                  array_size = np.size(test['arr_2'])
                  #plt.figure()
                  #ax1 = plt.subplot(1,1,1)
                  #ax1.plot(np.arange(0, array_size), test['arr_2'], '.-')
                  #ax1.set_ylabel('Correlation')
                  #ax1.set_xlabel('Field (mT)')

                  #ax2 = ax1.twiny()
                  #newlabel = [0, 1, 2, 3, 4]
                  corr = test['arr_2']
                  field = test['arr_1'][:, 1]*np.sin(np.pi/4)
                  #fieldsteps = np.arange(0, array_size+1, 84)
                  fieldsteps = np.arange(0, array_size)
                  fig, ax = plt.subplots(1,1)
                  ax.plot(fieldsteps, test['arr_2'], '.-')
                  ax.set_xticks(fieldsteps[::21])
                  ax.set_xticklabels(np.int_(np.rint(field[::21]*1000)))
                  #plt.plot(np.arange(0, array_size), test['arr_2'], '.-')
                  plt.vlines(np.arange(0, array_size+1, 84), min(corr)-0.02, 0.02+max(corr), linestyles = 'dashed')
                  plt.xlabel('Field (mT)')
                  plt.ylabel('Correlation')
                  plt.title('')
                  #plt.xticks(fieldsteps, np.around(field*1000, decimals = 0))
                  plt.ylim([min(corr)-0.02, 0.02+max(corr)])
                  print(root)
                  nameappend = root[root.find('Hc_std'):root.find(r'\\')]
                  #print(str(np.around(float(nameappend[6:])*100), decimals = 1))
                  #plt.title(r'RPM - Quenched Disorder '+ str(np.around(float(nameappend[6:])*100, decimals = 1))+r'%')
                  plt.savefig(r'C:\Users\av2813\Box\GitHub\RPM\RPM_Data\SquareMonte_HCstd2p5\Pictures\Correlation'+nameappend+'.png')
                  plt.savefig(r'C:\Users\av2813\Box\GitHub\RPM\RPM_Data\SquareMonte_HCstd2p5\Pictures\Correlation'+nameappend+'.svg')
                  #plt.figure()
                  #plt.plot(test['arr_1'][0:,1]*np.sin(np.pi/4.), test['arr_2'][0:], '.-')
                  plt.show()



# newfolder = r'C:\Users\av2813\Box\GitHub\RPM\RPM_Data\QuenchedDisorder_variation\square7\Hc_std1.000000e-01'
# energy = []
# counter = []
# for root, dirs, files in os.walk(newfolder):
#     for file in files:
#         if 'Lattice_counter' in file:
#             #print(file)
#             #print(file.find('counter'))
#             #print(file[file.find('counter'):18])
#             print(int(re.findall(r'\d+', file[file.find('counter'):18])[0]))
#             t = int(re.findall(r'\d+', file[file.find('counter'):18])[0])
#             counter.append(t)
#             #print(int(filter(str.isdigit, file)))
#             #print(((str.isdigit, file[file.find('counter'):18])))
#             #print([int(s) for s in str.split() if s.isdigit()])
#             #counter.append(file[])
#             lattice = rpm.ASI_RPM(1,1)
#             lattice.load(os.path.join(root, file))
#             #lattice.graph()
#             eng = lattice.demagEnergy(3)
#             print(eng)
#             energy.append(eng)

# plt.figure()
# plt.plot(counter, energy, '.')
# plt.show()




