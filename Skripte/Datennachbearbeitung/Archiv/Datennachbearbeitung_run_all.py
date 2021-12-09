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
			pwm = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights.npy')
			pwm = pwm[:,6804:(6804+176)]
			pred = np.load('D:\Masterarbeit\Predictions\\'+datei+'\\'+datei+'.npy')
			for i in range(0,pwm.shape[0]):
				altpwm = np.asarray(pwm[i,])[np.newaxis]
				prepwm = np.asarray(pred[i,])[np.newaxis]
				x = kl_divergence_by_christian(altpwm,prepwm)
				tsvdateimitdivergencen.write(str(np.asarray(x[0,]))+'\n')
		elif ('prediction' in datei) & ('140' in datei):
			tsvdateimitdivergencen = open('D:\Masterarbeit\Predictions'+'\\'+datei+'\kl_divergencen.tsv','w')
			pwm = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMsGruppen_Zuordnung_Weights.npy')
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
def takeSecond(elem):
	return elem[1]
def auswertung_in_list():
	pfadpredpwms = os.listdir('D:\Masterarbeit\Predictions')
	auswertungsdatei = open('D:\Masterarbeit\Predictions\AuswertungNeuronaleNetze.tsv','w')
	list = []
	for datei in pfadpredpwms:
		if 'prediction' in datei:
			dl_kl_gegen = open('D:\Masterarbeit\Predictions\\'+datei+'\\Durchschnitt_kl_divergencenGegenListe.tsv')
			dl_kl_gegenZ = dl_kl_gegen.readlines()
			list.append((datei, float(dl_kl_gegenZ[0])))
	list.sort(key = takeSecond)
	for element in list:
		auswertungsdatei.write(str(element[0])+'\t'+str(element[1])+'\n')



Berechne_KL_Divergence_Ohne_PWMs_erzeugen()
Durchschnitt_KL_Divergence()
auswertunggegenliste()
durchschnittkldiv()
auswertung_in_list()
