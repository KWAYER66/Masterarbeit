import os, sys
import numpy as np
from numpy import genfromtxt
from numpy import savetxt
import fnmatch

dbd = os.listdir('D:\Masterarbeit\DBDs')
kl_div = open('D:\Masterarbeit\Predictions\prediction002_176_1_1_4_500\kl_divergencentestdata.tsv')
kl_divZ = kl_div.readlines()
if os.path.exists('D:\Masterarbeit\DBDsKL_DIVtest') == False:
    os.makedirs('D:\Masterarbeit\DBDsKL_DIVtest')

for folder in dbd:
    if 'ergebnis' not in folder:
        dbdkl_div_datei = open('D:\Masterarbeit\DBDsKL_DIVtest\\'+folder+'.tsv', 'w')
        folderlist = os.listdir('D:\Masterarbeit\DBDs\\'+folder)
        for pwmdatei in folderlist:
            for Zeile in range(0,len(kl_divZ)):
                if pwmdatei.split('.')[0] in kl_divZ[Zeile]:
                    print(kl_divZ[Zeile])
                    dbdkl_div_datei.write(kl_divZ[Zeile])
