import os, sys
import numpy as np
from numpy import genfromtxt
from numpy import savetxt
import fnmatch


durchschnitt_dbd = open('D:\Masterarbeit\DBDsmedianKL_DIVtest2.tsv', 'w')
dbdkl_div = os.listdir('D:\Masterarbeit\DBDsKL_DIVtest')

for datei in dbdkl_div:
    durchschnitt_dbd.write(datei.split('.')[0]+'.'+datei.split('.')[1]+'\t')
    oeffnekl_div = open('D:\Masterarbeit\DBDsKL_DIVtest\\'+datei)
    oeffnekl_divZ = oeffnekl_div.readlines()
    arr = []
    for i in range(0, len(oeffnekl_divZ)):
        arr.append(float(oeffnekl_divZ[i].split('\t')[1]))
    arr = np.sort(arr)
    if len(arr) == 1:
        durchschnitt_dbd.write(str(arr[0])+'\t'+str(len(arr))+'\n')
    elif len(arr) % 2 == 0:
        durchschnitt_dbd.write(str(arr[int(len(arr)/2)])+'\t'+str(len(arr))+'\n')
    elif len(arr) % 2 != 0:
        durchschnitt_dbd.write(str(arr[int(len(arr)/2-0.5)])+'\t'+str(len(arr))+'\n')
