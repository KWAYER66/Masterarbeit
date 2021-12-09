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


def kl_divergence_by_christian(y_true, y_pred):
	y_pred = ops.convert_to_tensor_v2_with_dispatch(y_pred)
	y_true = math_ops.cast(y_true, y_pred.dtype)
	y_true = backend.clip(y_true, backend.epsilon(), 1)
	y_pred = backend.clip(y_pred, backend.epsilon(), 1)
	return math_ops.reduce_sum(y_true * math_ops.log(y_true / y_pred), axis=-1)
def Berechne_KL_Divergence_Ohne_PWMs_erzeugen():
	pfadpredpwms = os.listdir('D:\Masterarbeit\Predictions')
	for datei in pfadpredpwms:
		if ('prediction' in datei) & ('176' in datei):
			tsvdateimitdivergencen = open('D:\Masterarbeit\Predictions'+'\\'+datei+'\kl_divergencen.tsv','w')
			pwm = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights_Abst_tf.npy')
			pwm = pwm[:,6804:(6804+176)]
			pred = np.load('D:\Masterarbeit\Predictions\\'+datei+'\\'+datei+'.npy')
			for i in range(0,pwm.shape[0]):
				altpwm = np.asarray(pwm[i,])[np.newaxis]
				prepwm = np.asarray(pred[i,])[np.newaxis]
				x = kl_divergence_by_christian(altpwm,prepwm)
				#tsvdateimitdivergencen.write(str(np.asarray(x[0,]))+'\n')


				prepwm2 = np.flip(prepwm)
				x2 = kl_divergence_by_christian(altpwm,prepwm2)
				if float(x[0]) < float(x2[0]):
					tsvdateimitdivergencen.write(str(np.asarray(x[0,]))+'\t')
					tsvdateimitdivergencen.write(str(1)+'\n')
				else:
					tsvdateimitdivergencen.write(str(np.asarray(x2[0,]))+'\t')
					tsvdateimitdivergencen.write(str(-1)+'\n')
		elif ('prediction' in datei) & ('140' in datei):
			tsvdateimitdivergencen = open('D:\Masterarbeit\Predictions'+'\\'+datei+'\kl_divergencen.tsv','w')
			pwm = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights_Abst_tf.npy')
			pwm = pwm[:,6804:(6804+140)]
			pred = np.load('D:\Masterarbeit\Predictions\\'+datei+'\\'+datei+'.npy')
			for i in range(0,pwm.shape[0]):
				altpwm = np.asarray(pwm[i,])[np.newaxis]
				prepwm = np.asarray(pred[i,])[np.newaxis]
				x = kl_divergence_by_christian(altpwm,prepwm)
				tsvdateimitdivergencen.write(str(np.asarray(x[0,]))+'\n')
def auswertunggegenliste():
	listspfad = os.listdir('D:\Masterarbeit\Daten\Liste_Train_Test_Split')
	x = 'D:\Masterarbeit\Predictions'
	predictionsneuronalenetze = os.listdir(x)
	for file in predictionsneuronalenetze:
		if 'prediction' in file:
			for lists in listspfad:
				if 'gegenzufallsliste'+file.split('_')[4] in lists:
					print(lists)
					liste = np.sort(np.load('D:\Masterarbeit\Daten\Liste_Train_Test_Split\\'+lists))
					kl_div = open(x+'\\'+file+'\\kl_divergencen.tsv')
					kl_divGegen = open(x+'\\'+file+'\\kl_divergencenGegenListe.tsv', 'w')
					kl_divGegenPlot = open(x+'\\'+file+'\\kl_divergencenGegenListePlot.tsv', 'w')
					kl_divZ = kl_div.readlines()
					for i in range(0,len(kl_divZ)):
						for j in range(0, len(liste)):
							if i == liste[j]:
								kl_divGegen.write(kl_divZ[i])
								kl_divGegenPlot.write(kl_divZ[i])
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
				divergencen = divergencen + float(kl_divGegenZ[i])
				divergencenzaehler = divergencenzaehler + 1
			durchschnittkl_divGegen.write(str(divergencen/divergencenzaehler) +'\n')
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
				durchschnitt = durchschnitt + float(kl_div_alleZ[i])
				j = i
			if j > 0:
				durchschnitt = durchschnitt / j
			ausgabedatei.write(str(durchschnitt)+'\n')
def median_kl_div_all():
	pfad = os.listdir('D:\Masterarbeit\Predictions')
	for datei in pfad:
		if 'prediction' in datei:
			ausgabedatei = open('D:\Masterarbeit\Predictions'+'\\'+datei+'\\mediankl_div.tsv', 'w')
			kl_div_alle = open('D:\Masterarbeit\Predictions'+'\\'+datei+'\\kl_divergencen.tsv')
			kl_div_alleZ =kl_div_alle.readlines()
			median = 0
			j=0
			listekl_div = []
			for i in range(0, len(kl_div_alleZ)):
				listekl_div.append(float(kl_div_alleZ[i].split('\t')[0]))
				j = i
			listekl_div.sort()
			if j > 0:
				if len(listekl_div) % 2 != 0:
					median = listekl_div[int((len(listekl_div)-1)/2)]
				else:
					median = listekl_div[int((len(listekl_div)-2)/2)]
			else:
				median = listekl_div[0]
			ausgabedatei.write(str(median)+'\n')
def median_kl_div_testdata():
	listspfad = os.listdir('D:\Masterarbeit\Daten\Liste_Train_Test_Split')
	x = 'D:\Masterarbeit\Predictions'
	predictionsneuronalenetze = os.listdir(x)
	for file in predictionsneuronalenetze:
		if 'prediction' in file:
			for lists in listspfad:
				if 'gegenzufallsliste'+file.split('_')[4] in lists:
					liste = np.sort(np.load('D:\Masterarbeit\Daten\Liste_Train_Test_Split\\'+lists))
					kl_div = open(x+'\\'+file+'\\kl_divergencen.tsv')
					kl_div_plot_median = open(x+'\\'+file+'\\kl_div_median_testdata.tsv', 'w')
					kl_divZ = kl_div.readlines()
					listekl_div = []
					median = 0
					for i in range(0,len(kl_divZ)):
						for j in range(0, len(liste)):
							if i == liste[j]:
								listekl_div.append(kl_divZ[i].split('\t')[0])
					listekl_div.sort()
					if len(listekl_div) > 0:
						if len(listekl_div) % 2 != 0:
							median = listekl_div[int((len(listekl_div)-1)/2)]
						else:
							median = listekl_div[int((len(listekl_div)-2)/2)]
					else:
						median = listekl_div[0]
					kl_div_plot_median.write(str(median)+'\n')
def takeSecond(elem):
	return elem[1]
def auswertung_Durchschnitt_KL_Div():
	pfadpredpwms = os.listdir('D:\Masterarbeit\Predictions')
	auswertungsdatei = open('D:\Masterarbeit\Predictions\AuswertungNeuronaleNetze_Durchschnitt_KL_Div.tsv','w')
	list = []
	for datei in pfadpredpwms:
		if 'prediction' in datei:
			dl_kl_gegen = open('D:\Masterarbeit\Predictions\\'+datei+'\\Durchschnitt_kl_divergencenGegenListe.tsv')
			dl_kl_gegenZ = dl_kl_gegen.readlines()
			list.append((datei, float(dl_kl_gegenZ[0])))
	list.sort(key = takeSecond)
	for element in list:
		auswertungsdatei.write(str(element[0])+'\t'+str(element[1])+'\n')
def auswertung_Median_KL_Div():
	pfadpredpwms = os.listdir('D:\Masterarbeit\Predictions')
	auswertungsdatei = open('D:\Masterarbeit\Predictions\AuswertungNeuronaleNetze_Median_KL_Div.tsv','w')
	list = []
	for datei in pfadpredpwms:
		if 'prediction' in datei:
			dl_kl_gegen = open('D:\Masterarbeit\Predictions\\'+datei+'\\kl_div_median_testdata.tsv')
			dl_kl_gegenZ = dl_kl_gegen.readlines()
			list.append((datei, float(dl_kl_gegenZ[0])))
	list.sort(key = takeSecond)
	for element in list:
		auswertungsdatei.write(str(element[0])+'\t'+str(element[1])+'\n')
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
			kl_div = open('D:\Masterarbeit\Predictions'+'\\'+datei+'\kl_divergencen.tsv')
			kl_divZ = kl_div.readlines()
			for datei2 in prediction:
				if ('prediction' in datei2):
					preds = np.load(verzeichnispfad+'\\'+datei+'\\'+datei2, 'r')


			i=0
			zaehler = 0
			for file in pwmsnamen:
				if int(kl_divZ[i].split('\t')[1]) == -1:
				#	print(preds[i,:])
					predswrite = np.flip(preds[i,:])
				else:
					predswrite = preds[i,:]



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
def Berechne_KL_Divergence():
	pfadinputpwms = 'D:\Masterarbeit\Daten\PWM_shifts_full_ueberarbeitet'
	pfadinputpwmsG = 'D:\Masterarbeit\Daten\PWMS_Nach_Gruppen_ueberarbeitet\AlleZusammen'
	listpwmsnamen = os.listdir(pfadinputpwms)
	listpwmsnamenG = os.listdir(pfadinputpwmsG)

	pfadpredpwms = os.listdir('D:\Masterarbeit\Predictions')

	for datei in pfadpredpwms:
		if ('prediction' in datei) & ('176' in datei):
			tsvdateimitdivergencen = open('D:\Masterarbeit\Predictions'+'\\'+datei+'\kl_divergencen2.tsv','w')
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
			tsvdateimitdivergencen = open('D:\Masterarbeit\Predictions'+'\\'+datei+'\kl_divergencen2.tsv','w')
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
def testgruppenzuordnung():
    predictionverzeichnis = os.listdir('D:\Masterarbeit\Predictions')
    data = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights_Abst_tf.npy')[:,(6804+176):(6804+176+51)]
    for predictionordner in predictionverzeichnis:
        if 'prediction' in predictionordner:
            predictionordnerverzeichnis = os.listdir('D:\Masterarbeit\Predictions\\'+predictionordner)
            for file in predictionordnerverzeichnis:
                if 'zuordnung' in file:

                    ausgabezuordnung = open('D:\Masterarbeit\Predictions\\'+predictionordner+'\\zuordgruppenplotdaten.tsv','w')
                    #testlist = np.load('D:\Masterarbeit\Daten\Liste_Train_Test_Split\gegenzufallsliste'+str(predictionordner.split('_')[4])+'.npy')
                    #traininglist = np.load('D:\Masterarbeit\Daten\Liste_Train_Test_Split\zufallsliste'+str(predictionordner.split('_')[4])+'.npy')
                    zuordnungsfile = np.load('D:\Masterarbeit\Predictions\\'+predictionordner+'\\'+file)
                    for i in range(0, zuordnungsfile.shape[0]):
                        ausgabezuordnung.write(str(np.argmax(data[i,:]))+'\t')
                        ausgabezuordnung.write(str(np.argmax(zuordnungsfile[i,:]))+'\n')
def testgruppenzuordnungtestdata():
    predictionverzeichnis = os.listdir('D:\Masterarbeit\Predictions')
    listspfad = os.listdir('D:\Masterarbeit\Daten\Liste_Train_Test_Split')
    data = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights_Abst_tf.npy')[:,(6804+176):(6804+176+51)]
    for predictionordner in predictionverzeichnis:
        if 'prediction' in predictionordner:
            predictionordnerverzeichnis = os.listdir('D:\Masterarbeit\Predictions\\'+predictionordner)
            for file in predictionordnerverzeichnis:
                if 'zuordnung' in file:
                    for lists in listspfad:
                        if 'gegenzufallsliste'+file.split('_')[4] in lists:
                            liste = np.sort(np.load('D:\Masterarbeit\Daten\Liste_Train_Test_Split\\'+lists))
                            ausgabezuordnung = open('D:\Masterarbeit\Predictions\\'+predictionordner+'\\zuordgruppenplottestdaten.tsv','w')
                            zuordnungsfile = np.load('D:\Masterarbeit\Predictions\\'+predictionordner+'\\'+file)
                            for i in range(0, zuordnungsfile.shape[0]):
                                for j in range(0, len(liste)):
                                    if i == liste[j]:
                                        ausgabezuordnung.write(str(np.argmax(data[i,:]))+'\t')
                                        ausgabezuordnung.write(str(np.argmax(zuordnungsfile[i,:]))+'\n')

Berechne_KL_Divergence_Ohne_PWMs_erzeugen()
#Durchschnitt_KL_Divergence()
auswertunggegenliste()
#durchschnittkldiv()
median_kl_div_all()
median_kl_div_testdata()
#auswertung_Durchschnitt_KL_Div()
auswertung_Median_KL_Div()
ListRepresentantMitKLDIV_ListAndereMitKL_DIV()
SplitPredictionsInSinglePwmData()
#Berechne_KL_Divergence()
#testgruppenzuordnung()
#testgruppenzuordnungtestdata()
