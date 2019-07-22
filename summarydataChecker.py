import rpmClass_Stable as rpm
import os
import csv
import numpy as np

#folder = os.getcwd()

folder = r'D:\RPM_Rapid\ShaktiSSF_QDvsHapp2\ShaktiPD_QD1.000000e-02_Happ1.070000e-01_count9'

if os.path.isfile(os.path.join(folder, 'SummaryData.csv')) == False:
	a = [s for s in os.listdir(folder) if os.path.isfile(os.path.join(folder, s)) and '.npz' in s]
	a.sort(key=lambda s: os.path.getmtime(os.path.join(folder, s)))					
	file = a[-1]
	file_prev = a[-3]
	Lattice_prev = rpm.ASI_RPM(1,1)
	Lattice_prev.load(os.path.join(folder, file))
	print(file)
	Lattice = rpm.ASI_RPM(1,1)
	Lattice.load(os.path.join(folder, file))
	tcycles = Lattice.sortFunc2(file, 'Counter', '_Lattice')
	period = np.nan
	loops = tcycles
	Hmax = float(Lattice.sortFunc(file, 'Happlied', 'T_H', integer = False).replace('p', '.'))
	Htheta = float(Lattice.sortFunc(file, 'Htheta', 'Rad_', integer = False).replace('p', '.'))
	Mag = Lattice.netMagnetisation()
	Mx = Mag[0]
	My = Mag[1]
	Mtot = Mx +My
	corr = Lattice.correlation(Lattice_prev, Lattice)
	Hloc_mean, Hloc_std = Lattice.localFieldParameters()
	summarydata = [[Lattice.returnHc(), Lattice.returnHc_std(), Hmax, Htheta, tcycles, period, loops, Lattice.returnLength(),\
	         Lattice.returnVGap(), Lattice.returnWidth(), Lattice.returnThickness(), Lattice.returnMs(), Lattice.returnUCx(), \
	         Lattice.returnUCy(), Lattice.estInteractionStr(), Lattice.EtotalCalc(), Mx,My, Mtot, Hloc_mean, Hloc_std,\
	         Lattice.monopoleDensity(),corr]]
	with open(os.path.join(folder, "SummaryData.csv"), "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(np.array(summarydata).tolist())

