import os, sys
import numpy as np
from numpy import genfromtxt
from numpy import savetxt

#sys.argv[1] = verzeichnispfad in dem die predictions sind
pfad = os.listdir(sys.argv[1])


for datei in pfad:
	if 'predictions' in datei:
		if 'npy' not in datei:
			ausgabedatei = open(sys.argv[1]+'\\'+datei+'\\durchschnittlichekl_div.tsv', 'w')
			kl_div_alle = open(sys.argv[1]+'\\'+datei+'\\kl_divergencen.tsv')
			kl_div_alleZ =kl_div_alle.readlines()
			durchschnitt = 0
			j=0
			for i in range(0, len(kl_div_alleZ)):
				if 'M' in kl_div_alleZ[i]:
					durchschnitt = durchschnitt + float(kl_div_alleZ[i].split('\t')[1])
					j = i
			if j > 0:
				durchschnitt = durchschnitt / j
			ausgabedatei.write(str(durchschnitt)+'\n')
