import numpy as np
from numpy import genfromtxt
from numpy import savetxt
import sys
import os


def ListRepresentantMitKLDIV_ListAndereMitKL_DIV():
	listspfad = os.listdir('D:\Masterarbeit\Daten\Liste_Train_Test_Split')
	Pwms = os.listdir('D:\Masterarbeit\Daten\PWM_shifts_full_ueberarbeitet')
	data = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights_Abst_tf.npy')[:,6804+176+51]
	predictions = os.listdir('D:\Masterarbeit\Predictions')
	for prediction in predictions:
		if 'prediction' in prediction:

			kl_div = open('D:\Masterarbeit\Predictions\\'+prediction+'\kl_divergencen.tsv')
			kl_divZ = kl_div.readlines()

			#Hier separiert Representant und Andere (ALLE)
			AusgabeRepresentanten = open('D:\Masterarbeit\Predictions\\'+prediction+'\kl_divergencenrepresentanten.tsv','w')
			AusgabeAndere = open('D:\Masterarbeit\Predictions\\'+prediction+'\kl_divergencenandere.tsv','w')
			for i in range(0, data.shape[0]):
				if data[i] == 1:
					AusgabeRepresentanten.write(str(Pwms[i])+'\t')
					AusgabeRepresentanten.write(str(kl_divZ[i])+'\n')
				else:
					AusgabeAndere.write(str(Pwms[i])+'\t')
					AusgabeAndere.write(str(kl_divZ[i])+'\n')
			AusgabeRepresentanten.close()
			AusgabeAndere.close()

			#Hier separiert Representant und Andere (Testdata)
			AusgabeRepresentanten = open('D:\Masterarbeit\Predictions\\'+prediction+'\kl_divergencenrepresentantentestdata.tsv','w')
			AusgabeAndere = open('D:\Masterarbeit\Predictions\\'+prediction+'\kl_divergencenanderetestdata.tsv','w')
			print('For Schleife Testdata')
			for lists in listspfad:
				if 'gegenzufallsliste'+prediction.split('_')[4] in lists:
					print('testgegenzufallsliste'+prediction.split('_')[4])
					liste = np.sort(np.load('D:\Masterarbeit\Daten\Liste_Train_Test_Split\\'+lists))
					print(lists)
					print(liste.shape)
					for i in range(0, data.shape[0]):
						for j in range(0, len(liste)):
							if i == liste[j]:
								if data[i] == 1:
									AusgabeRepresentanten.write(str(Pwms[i])+'\t')
									AusgabeRepresentanten.write(str(kl_divZ[i])+'\n')
								else:
									AusgabeAndere.write(str(Pwms[i])+'\t')
									AusgabeAndere.write(str(kl_divZ[i])+'\n')
			AusgabeRepresentanten.close()
			AusgabeAndere.close()

			#Hier separiert Representant und Andere (Traindata)
			AusgabeRepresentanten = open('D:\Masterarbeit\Predictions\\'+prediction+'\kl_divergencenrepresentantentraindata.tsv','w')
			AusgabeAndere = open('D:\Masterarbeit\Predictions\\'+prediction+'\kl_divergencenanderetraindata.tsv','w')
			for lists in listspfad:
				if 'zufallsliste'+prediction.split('_')[4]+'.npy' == lists:
					liste = np.sort(np.load('D:\Masterarbeit\Daten\Liste_Train_Test_Split\\'+lists))
					for i in range(0, data.shape[0]):
						for j in range(0, len(liste)):
							if i == liste[j]:
								if data[i] == 1:
									AusgabeRepresentanten.write(str(Pwms[i])+'\t')
									AusgabeRepresentanten.write(str(kl_divZ[i])+'\n')
								else:
									AusgabeAndere.write(str(Pwms[i])+'\t')
									AusgabeAndere.write(str(kl_divZ[i])+'\n')
			AusgabeRepresentanten.close()
			AusgabeAndere.close()

ListRepresentantMitKLDIV_ListAndereMitKL_DIV()
