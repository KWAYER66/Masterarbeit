import os, sys
import numpy as np
from numpy import genfromtxt
from numpy import savetxt

#sys.argv[1] = verzeichnispfad in dem die predictions sind
pfadpwmshiftsgruppen = 'D:\Inferenz_von_TF_Bindepraeferenzen\PWMS_Nach_Gruppen_korrekt'
pwmshiftsgruppen = os.listdir(pfadpwmshiftsgruppen)
pfad = os.listdir(sys.argv[1])


for datei in pfad:
	if ('predictions1' in datei):
		if 'npy' not in datei:
			kl_div = open(sys.argv[1]+'\\'+datei+'\\kl_divergencen.tsv')
			kl_divZ = kl_div.readlines()
			for file2 in pwmshiftsgruppen:
				if 'PWM_shifts_TF' in file2:
					durchschnitt = 0
					zaehler=0
					ausgabedatei = open(sys.argv[1]+'\\'+datei+'\\'+file2+'.tsv','w')
					pwmshiftgruppe = os.listdir('D:\Inferenz_von_TF_Bindepraeferenzen\PWMS_Nach_Gruppen_korrekt\\'+file2)
					for file in pwmshiftgruppe:
						ausgabedatei.write(file+'\t')
						for i in range(0,len(kl_divZ)):
							if (kl_divZ[i]!='\n') & (file.split('.')[0] == kl_divZ[i].split('\t')[0].split('.')[0]):
								durchschnitt = durchschnitt + float(kl_divZ[i].split('\t')[1])
								zaehler = zaehler + 1
								ausgabedatei.write(kl_divZ[i].split('\t')[1]+'\n')
					ausgabedatei.write('durchschnitt\t'+str(durchschnitt/zaehler))
