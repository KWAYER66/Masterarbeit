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

def SplitPredictionsInSinglePwmData():
	verzeichnispfad = 'D:\Masterarbeit\Predictions'
	pwmsnamen = os.listdir('D:\Masterarbeit\Daten\PWM_shifts_full_ueberarbeitet')
	pwmsnamen.sort()
	verzeichnispfadlist = os.listdir(verzeichnispfad)
	for datei in verzeichnispfadlist:
		if ('prediction' in datei):
			if os.path.exists(verzeichnispfad+'\\'+datei+'\\pdfs') == False:
				os.makedirs(verzeichnispfad+'\\'+datei+'\\pdfs')
			prediction = os.listdir(verzeichnispfad+'\\'+datei)
			for datei2 in prediction:
				if ('prediction' in datei2):
					preds = np.load(verzeichnispfad+'\\'+datei+'\\'+datei2, 'r')
			i=0
			for file in pwmsnamen:
				ausgabe = open(verzeichnispfad+'\\'+datei+'\\'+file, 'w')
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
def kl_divergence_by_christian(y_true, y_pred):
  y_pred = ops.convert_to_tensor_v2_with_dispatch(y_pred)
  y_true = math_ops.cast(y_true, y_pred.dtype)
  y_true = backend.clip(y_true, backend.epsilon(), 1)
  y_pred = backend.clip(y_pred, backend.epsilon(), 1)
  return math_ops.reduce_sum(y_true * math_ops.log(y_true / y_pred), axis=-1)
def Berechne_KL_Divergence():
	pfadinputpwms = 'D:\Masterarbeit\Daten\PWM_shifts_full_ueberarbeitet'
	pfadinputpwmsG = 'D:\Masterarbeit\Daten\PWMS_Nach_Gruppen_ueberarbeitet\AlleZusammen'
	listpwmsnamen = os.listdir(pfadinputpwms)
	listpwmsnamenG = os.listdir(pfadinputpwmsG)

	pfadpredpwms = os.listdir('D:\Masterarbeit\Predictions')

	for datei in pfadpredpwms:
		if ('prediction' in datei) & ('176' in datei):
			tsvdateimitdivergencen = open('D:\Masterarbeit\Predictions'+'\\'+datei+'\kl_divergencen.tsv','w')
			for file in listpwmsnamen:
				if 'pwm' in file:
					inputpwm = open(pfadinputpwms+"\\"+file)
					pwmZ = inputpwm.readlines()
					predpwm = open('D:\Masterarbeit\Predictions'+'\\'+datei+"\\"+file)
					predZ = predpwm.readlines()

					pwmlist1 = []
					pwmlist2 = []
					for i in range(1,len(pwmZ)):
						for j in range(0,4):
							pwmlist1.append(float(pwmZ[i].split('\n')[0].split('\t')[j]))
							pwmlist2.append(float(predZ[i].split('\n')[0].split('\t')[j]))
					altpwm = np.asarray(pwmlist1)[np.newaxis]
					prepwm = np.asarray(pwmlist2)[np.newaxis]
					x = kl_divergence_by_christian(altpwm,prepwm)
					tsvdateimitdivergencen.write(file.split('.')[0]+'.'+file.split('.')[1]+'\t')
					tsvdateimitdivergencen.write(str(np.asarray(x[0,]))+'\n')
		elif ('prediction' in datei) & ('140' in datei):
			tsvdateimitdivergencen = open('D:\Masterarbeit\Predictions'+'\\'+datei+'\kl_divergencen.tsv','w')
			for file in listpwmsnamenG:
				if 'pwm' in file:
					inputpwm = open(pfadinputpwmsG+'\\'+file)
					pwmZ = inputpwm.readlines()
					predpwm = open('D:\Masterarbeit\Predictions'+'\\'+datei+"\\"+file)
					predZ = predpwm.readlines()

					pwmlist1 = []
					pwmlist2 = []
					for i in range(1,len(pwmZ)):
						for j in range(0,4):
							pwmlist1.append(float(pwmZ[i].split('\n')[0].split('\t')[j]))
							pwmlist2.append(float(predZ[i].split('\n')[0].split('\t')[j]))
					altpwm = np.asarray(pwmlist1)[np.newaxis]
					prepwm = np.asarray(pwmlist2)[np.newaxis]
					x = kl_divergence_by_christian(altpwm,prepwm)
					tsvdateimitdivergencen.write(file.split('.')[0]+'.'+file.split('.')[1]+'\t')
					tsvdateimitdivergencen.write(str(np.asarray(x[0,]))+'\n')
def Durchschnitt_KL_Divergence():
	pfad = os.listdir('D:\Masterarbeit\Predictions')
	for datei in pfad:
		if 'prediction' in datei:
			ausgabedatei = open('D:\Masterarbeit\Predictions'+'\\'+datei+'\\durchschnittlichekl_div.tsv', 'w')
			kl_div_alle = open('D:\Masterarbeit\Predictions'+'\\'+datei+'\\kl_divergencen.tsv')
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
def KL_Divergence_Pro_Gruppe():
	pfadpwmshiftsgruppen = 'D:\Masterarbeit\Daten\PWMS_Nach_Gruppen_ueberarbeitet'
	pwmshiftsgruppen = os.listdir(pfadpwmshiftsgruppen)
	pfad = os.listdir('D:\Masterarbeit\Predictions')


	for datei in pfad:
		if ('prediction' in datei):
				kl_div = open('D:\Masterarbeit\Predictions'+'\\'+datei+'\\kl_divergencen.tsv')
				kl_divZ = kl_div.readlines()
				for file2 in pwmshiftsgruppen:
					if 'PWM_shifts_TF' in file2:
						durchschnitt = 0
						zaehler=0
						ausgabedatei = open('D:\Masterarbeit\Predictions'+'\\'+datei+'\\'+file2+'.tsv','w')
						pwmshiftgruppe = os.listdir('D:\Masterarbeit\Daten\PWMS_Nach_Gruppen_ueberarbeitet\\'+file2)
						for file in pwmshiftgruppe:
							ausgabedatei.write(file+'\t')
							for i in range(0,len(kl_divZ)):
								if (kl_divZ[i]!='\n') & (file.split('.')[0] == kl_divZ[i].split('\t')[0].split('.')[0]):
									durchschnitt = durchschnitt + float(kl_divZ[i].split('\t')[1])
									zaehler = zaehler + 1
									ausgabedatei.write(kl_divZ[i].split('\t')[1]+'\n')
						ausgabedatei.write('durchschnitt\t'+str(durchschnitt/zaehler))
def erzeugezufallsliste(x):
	data = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights.npy')
	rng = default_rng()
	for i in range(0,x):
  	  liste1 = rng.choice(range(0,len(data)), size =1500, replace = False)
  	  np.save('D:\Masterarbeit\Daten\Liste_Train_Test_Split\zufallsliste'+str(i)+'.npy',liste1)
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
				np.save('D:\Masterarbeit\Daten\Liste_Train_Test_Split\gegen'+lists,gegenliste)
def auswertunggegenliste():
	listspfad = os.listdir('D:\Masterarbeit\Daten\Liste_Train_Test_Split')
	x = 'D:\Masterarbeit\Predictions'
	for lists in listspfad:
		if 'gegenzufallsliste' in lists:
			liste = np.sort(np.load('D:\Masterarbeit\Daten\Liste_Train_Test_Split\\'+lists))
			predictionsneuronalenetze = os.listdir(x)
			for file in predictionsneuronalenetze:
				if 'prediction' in file:
					kl_div = open(x+'\\'+file+'\\kl_divergencen.tsv')
					kl_divGegen = open(x+'\\'+file+'\\kl_divergencenGegenListe.tsv', 'w')
					kl_divGegenPlot = open(x+'\\'+file+'\\kl_divergencenGegenListePlot.tsv', 'w')
					kl_divZ = kl_div.readlines()
					for i in range(0,len(kl_divZ)):
						for j in range(0, len(liste)):
							if i == liste[j]:
								kl_divGegen.write(kl_divZ[i])
								kl_divGegenPlot.write(kl_divZ[i].split('\t')[1])
def durchschnittkldiv():
	x = 'D:\Masterarbeit\Predictions'
	predictionsneuronalenetze = os.listdir(x)
	for file in predictionsneuronalenetze:
		if 'prediction' in file:
			divergencen = 0
			divergencenzaehler = 0
			durchschnittkl_divGegen = open(x+'\\'+file+'\\Durchschnitt_kl_divergencenGegenListe.tsv', 'w')
			kl_divGegen = open(x+'\\'+file+'\\kl_divergencenGegenListe.tsv')
			kl_divGegenZ = kl_divGegen.readlines()
			for i in range(0,len(kl_divGegenZ)):
				divergencen = divergencen + float(kl_divGegenZ[i].split('\t')[1])
				divergencenzaehler = divergencenzaehler + 1
			durchschnittkl_divGegen.write(str(divergencen/divergencenzaehler) +'\n')
SplitPredictionsInSinglePwmData()
Berechne_KL_Divergence()
Durchschnitt_KL_Divergence()
KL_Divergence_Pro_Gruppe()
#erzeugezufallsliste(5)
#erzeugegegenteilliste()
auswertunggegenliste()
durchschnittkldiv()
