import os, sys
import numpy as np
from numpy import genfromtxt
from numpy import savetxt
import tensorflow as tf
from tensorflow.python.ops import nn
from tensorflow.python.keras import backend
import tensorflow.keras.backend as K
from tensorflow.python.framework import ops
from tensorflow.python.ops import math_ops
from random import sample
from random import random
from numpy.random import default_rng


def erzeugezufallsliste():
	pwmsgruppen = os.listdir('D:\Masterarbeit\Daten\PWM_shifts_full_ueberarbeitet')
	data = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights_Abst_tf_neu3.npy')

	pwmallfile = open('D:\Masterarbeit\Daten\PWM.txt')
	pwmallfileZ = pwmallfile.readlines()
	dict_tffaktors = {}
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
	rng = default_rng()
	liste = list(dict_tffaktors.keys())
	#Erzeuge Zufallsliste
	for anzahlliste in range(1,6):
		doppeltzufalllistevermeiden = []
		zufallsliste = []
		i=0
		while i <=(data.shape[0]*0.75):
			zufallszahl = int(rng.choice(range(0,len(dict_tffaktors)), size = 1))
			#Test ob zufallszahl bereits in liste
			if zufallszahl not in doppeltzufalllistevermeiden:
				doppeltzufalllistevermeiden.append(zufallszahl)
				for k in range(0,len(dict_tffaktors[liste[zufallszahl]])):
					for pwm in range(0,len(pwmsgruppen)):
						if dict_tffaktors[liste[zufallszahl]][k] == pwmsgruppen[pwm]:
							zufallsliste.append(int(pwm))
				i = i + len(dict_tffaktors[liste[zufallszahl]])
		zufallsliste.sort()
		np.save('D:\Masterarbeit\Daten\Liste_Train_Test_Split\zufallsliste_neu'+str(anzahlliste)+'.npy',zufallsliste)

def erzeugegegenteilliste():
	listspfad = os.listdir('D:\Masterarbeit\Daten\Liste_Train_Test_Split')
	for lists in listspfad:
		if 'zufallsliste' in lists:
			liste = np.load('D:\Masterarbeit\Daten\Liste_Train_Test_Split\\'+lists)
			liste = np.sort(liste)
			gegenliste = []
			zaehler = 0
			for i in range(0,liste.shape[0]):
				if zaehler == liste[i]:
					zaehler = zaehler + 1
				elif zaehler != liste[i]:
					for j in range(0,liste[i]-zaehler):
						gegenliste.append(zaehler)
						zaehler = zaehler + 1
					zaehler = zaehler +1
			print(len(liste))
			print(len(gegenliste))
			np.save('D:\Masterarbeit\Daten\Liste_Train_Test_Split\gegenneu'+lists,gegenliste)


erzeugezufallsliste()
erzeugegegenteilliste()
