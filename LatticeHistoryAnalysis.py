import numpy as np
import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import csv

folder = r'D:\RPM_Rapid\SquareSSF_QDvHapp'
latticehistory = []
checkstring = 'LatticeHistory.csv'
counter = 0
for root, subs, files in os.walk(folder):
    for file in files:
        if checkstring in file:
            print(root, file)
            filename = os.path.join(root, file)
            LHistory = pd.read_csv(filename, sep = r',', header = None).values
            print(LHistory)
            latticehistory.append(LHistory)
            #for L in LHistory:
            #    print(L)
            #corrhistory.append(LHistory)
            #maghistory.append(LHistory)
            #print(filename)
            print(counter)
            #print(filename)
            #QD = sortFunc2(filename, 'PD_QD', '_Width')
            #tempdata = pd.read_csv(filename, delimiter = ',', header = None).values
            #print(tempdata[0,:])
            #tempdata2 = tempdata[0, :]
            #print(tempdata2)
            #summarydata.append(tempdata2)
            #print(tempdata)
            counter+=1
            if counter == 10:
                break
        if counter ==10:
            break
latticehistory = np.array(latticehistory)
np.save(os.path.join(folder, 'Square'), latticehistory)
lh = np.load(os.path.join(folder, 'Square.npy'))
print(lh)
print(latticehistory)
with open(os.path.join(folder, "SquareSSF_Lattice2History.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(latticehistory)