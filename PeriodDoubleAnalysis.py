import rpmClass_Stable as rpm
import numpy as np
import math
import os
import matplotlib.pyplot as plt
import seaborn as sns
import re
from importlib import *			#Package to update the version of rpmClass_Stable

reload(rpm)
sns.set_style("ticks")
sns.set_palette("colorblind")


Lattice = rpm.ASI_RPM(1, 1)

#folder = r'D:\RPM_Rapid\SquarePeriodDouble\PeriodDoublingData_QD1.000000e-01_Width4.200000e-07_Count3'
#folder = r'D:\RPM_Rapid\SquarePeriodDouble\PeriodDoublingData_QD1.000000e-01_Width3.800000e-07_Count5'
#folder = r'D:\RPM_Rapid\SquarePeriodDouble\PeriodDoublingData_QD8.000002e-02_Width2.600000e-07_Count1'
#folder= r'D:\RPM_Rapid\SquarePeriodDouble\PeriodDoublingData_QD6.400004e-02_Width3.400000e-07_Count3'

folder = r'D:\RPM_Rapid\TetrisPeriodDouble'
for root, subdirs, files in os.walk(folder):
	for sub in subdirs:
		if 'PeriodDoublingData' in sub:
			path, dirs, fi = next(os.walk(os.path.join(root, sub)))
			file_count = len(fi)
			if file_count > 240:
				savefolder = folder + '\\AnalysedData\\' + sub
				if not os.path.exists(savefolder):
					os.makedirs(savefolder)
				Lattice.periodDoubleAnalysis(path, savefolder)
				Lattice.folderAnalysis(path, savefolder)
				plt.close('all')

