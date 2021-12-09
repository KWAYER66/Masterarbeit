import os,sys
import numpy as np
from numpy import genfromtxt


#sys.argv[1] = verzeichnispfad in dem die predictions sind
#ausgangsdata = np.load('D:\Inferenz_von_TF_Bindepraeferenzen\AlignmentsPWMs.npy', 'r')
#ausgangsdataG = np.load('D:\Inferenz_von_TF_Bindepraeferenzen\AlignmentsPWMsNachGruppen.npy', 'r')

pwmsnamen = os.listdir('D:\Inferenz_von_TF_Bindepraeferenzen\PWM_shifts_full_korrekt')
pwmsnamen.sort()

verzeichnispfad = os.listdir(sys.argv[1])


for datei in verzeichnispfad:
	if ('predictions1' in datei) & ('npy' in datei):
		if os.path.exists(sys.argv[1]+'\\'+datei.split('.')[0]) == False:
			os.makedirs(sys.argv[1]+'\\'+datei.split('.')[0])
		if os.path.exists(sys.argv[1]+'\\'+datei.split('.')[0]+'\\pdfs') == False:
			os.makedirs(sys.argv[1]+'\\'+datei.split('.')[0]+'\\pdfs')
		preds = np.load(sys.argv[1]+'\\'+datei, 'r')
		i=0
		for file in pwmsnamen:
			ausgabe = open(sys.argv[1]+'\\'+datei.split('.')[0]+'\\'+file, 'w')
			ausgabe.write('>'+file.split('.')[0]+'.'+file.split('.')[1]+'\n')
			for j in range(0, preds.shape[1]):
				ausgabe.write(str(preds[i][j]))
				if (j==3):
					ausgabe.write('\n')
				elif (j>3) & ((j-3)%4==0):
					ausgabe.write('\n')
				else:
					ausgabe.write('\t')
			i = i +1
