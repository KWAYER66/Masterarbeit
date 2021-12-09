import numpy as np
import os
from collections import defaultdict
pwmsgruppen = os.listdir('D:\Masterarbeit\Daten\PWM_shifts_full_ueberarbeitet')
data1 = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights_Abst.npy')
data2 = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMsGruppen_Zuordnung_Weights_Abst.npy')
faktortfneurinput = np.zeros((data1.shape[0],1))

pwmallfile = open('D:\Masterarbeit\Daten\PWM.txt')
pwmallfileZ = pwmallfile.readlines()
dict_tffaktors = {}
tffaktorvorkommen = {}
motivids = []
#1. Erzeuge Dict keys = TF, values = list von motiv-ids
for pwm in pwmsgruppen:
    zaehler = 0
    for i in range(0, len(pwmallfileZ)):
        if pwm.split('.')[0]+'.'+pwm.split('.')[1] in pwmallfileZ[i]:
            tffaktor = pwmallfileZ[i-3].split('\t')[1].splitlines()[0]
            if tffaktor in dict_tffaktors:
                dict_tffaktors[tffaktor].append(pwm)
            else:
                dict_tffaktors[tffaktor] = list()
                dict_tffaktors[tffaktor].append(pwm)
#2. Erzeuge jeweils Ordner für DBD mit zugehörigen PWMS
for key in dict_tffaktors.keys():
	if os.path.exists('D:\Masterarbeit\DBDs\\'+key) == False:
		os.makedirs('D:\Masterarbeit\DBDs\\'+key)
	for i in range(0, len(dict_tffaktors[key])):
		pwmalt = open('D:\Masterarbeit\Daten\PWM_shifts_full_ueberarbeitet\\'+dict_tffaktors[key][i])
		pwmaltZ = pwmalt.readlines()
		pwmneu = open('D:\Masterarbeit\DBDs\\'+key+'\\'+dict_tffaktors[key][i],'w')
		for j in range(0, len(pwmaltZ)):
			pwmneu.write(pwmaltZ[j])
