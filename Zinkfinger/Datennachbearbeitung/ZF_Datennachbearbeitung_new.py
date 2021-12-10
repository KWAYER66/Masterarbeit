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

def CreateFolder(Path):
	if os.path.exists(Path) == False:
		os.makedirs(Path)
def erzeugegegenteilliste2():
	listspfad = os.listdir('D:\Masterarbeit\ZinkFinger\zufallsliste2')
	inputdata = genfromtxt('D:\Masterarbeit\ZinkFinger\Input_NeuronalesNetzAlignment2.tsv', delimiter="\t")
	for lists in listspfad:
		if 'zufallsliste' in lists:
			liste = np.load('D:\Masterarbeit\ZinkFinger\zufallsliste2\\'+lists)
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
			if zaehler < inputdata.shape[0]:
				print('hi')
			print(len(liste))
			print(len(gegenliste))
			np.save('D:\Masterarbeit\ZinkFinger\zufallsliste2\gegenneu'+lists,gegenliste)
def erzeugegegenteilliste5():
	listspfad = os.listdir('D:\Masterarbeit\ZinkFinger\zufallsliste5')
	inputdata = genfromtxt('D:\Masterarbeit\ZinkFinger\Input_NeuronalesNetzAlignment5.tsv', delimiter="\t")
	for lists in listspfad:
		if 'zufallsliste' in lists:
			liste = np.load('D:\Masterarbeit\ZinkFinger\zufallsliste5\\'+lists)
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
			if zaehler < inputdata.shape[0]:
				print('hi')
			print(len(liste))
			print(len(gegenliste))
			np.save('D:\Masterarbeit\ZinkFinger\zufallsliste5\gegenneu'+lists,gegenliste)
def kl_divergence_by_christian(y_true, y_pred):
	y_pred = ops.convert_to_tensor_v2_with_dispatch(y_pred)
	y_true = math_ops.cast(y_true, y_pred.dtype)
	y_true = backend.clip(y_true, backend.epsilon(), 1)
	y_pred = backend.clip(y_pred, backend.epsilon(), 1)


	kl_div = math_ops.reduce_sum(y_true * math_ops.log(y_true / y_pred), axis=-1)
	return kl_div
def kl_divergence_by_christian2(y_true, y_pred):
  y_pred = ops.convert_to_tensor_v2_with_dispatch(y_pred)
  y_true = math_ops.cast(y_true, y_pred.dtype)
  y_true = y_true[:,20:180]

  y_true = backend.clip(y_true, backend.epsilon(), 1)
  y_pred = backend.clip(y_pred, backend.epsilon(), 1)


  y_pred2 = y_pred[:,0:160]

  #for rev in range(0,2):
  for i in range(0,41):
	  if i%4==0:
	  	j = i + 160
	  	y_pred2 = y_pred[:,i:j]
	  	if i == 0:
		  	min = tf.expand_dims(math_ops.reduce_sum(y_true * math_ops.log(y_true / y_pred2), axis=-1), -1)
	  	else:
		  	min2 = tf.expand_dims(math_ops.reduce_sum(y_true * math_ops.log(y_true / y_pred2), axis=-1), -1)
		  	min = tf.concat([min, min2], axis = 1)
  newmin = tf.math.reduce_min(min, axis = 1).numpy()[0]
  #print(min)
  #print(newmin)
  #print(tf.math.reduce_min(min, axis = 1))
  argmin = tf.math.argmin(min, axis = 1).numpy()[0]
  #print(tf.math.argmin(min, axis = 1).numpy()[0])
  arr = [newmin,argmin]
  return arr
def KL_Div_ohne_Pwms_erzeugen():
	pfadpredpwms = os.listdir('D:\Masterarbeit\ZinkFinger\Predictions')
	for datei in pfadpredpwms:
		if ('prediction' in datei):
			print('losgehts')
			pwm = genfromtxt('D:\Masterarbeit\ZinkFinger\Input_NeuronalesNetzAlignment3.tsv', delimiter="\t")
			print(pwm.shape)
			tsvdateimitdivergencen = open('D:\Masterarbeit\ZinkFinger\Predictions'+'\\'+datei+'\kl_divergencen.tsv','w')
			pwm = pwm[:,32076:32276]
			pred = np.load('D:\Masterarbeit\ZinkFinger\Predictions\\'+datei+'\\pwms.npy')
			for i in range(0,pwm.shape[0]):
			#for i in range(0,10):
				#print('hallo')
				altpwm = np.asarray(pwm[i,])[np.newaxis]
				prepwm = np.asarray(pred[i,])[np.newaxis]
				x = kl_divergence_by_christian2(altpwm,prepwm)
				prepwm2 = np.flip(prepwm)
				x2 = kl_divergence_by_christian2(altpwm,prepwm2)
				if float(x[0]) < float(x2[0]):
					tsvdateimitdivergencen.write(str(x[0])+'\t')
					tsvdateimitdivergencen.write(str(int(x[1]*4))+'\t')
					tsvdateimitdivergencen.write(str(1)+'\n')
				else:
					tsvdateimitdivergencen.write(str(x2[0])+'\t')
					tsvdateimitdivergencen.write(str(int(x2[1]*4))+'\t')
					tsvdateimitdivergencen.write(str(-1)+'\n')
				#x2 = kl_divergence_by_christian2(altpwm,prepwm2)

				#tsvdateimitdivergencen.write(str(np.asarray(x2[0]))+'\t')
				#tsvdateimitdivergencen.write(str(np.asarray(x2[1]))+'\n')
def SplitPredictionsInSinglePwmData():
	verzeichnispfad = 'D:\Masterarbeit\ZinkFinger\Predictions'
	pwmsnamen = os.listdir('D:\Masterarbeit\ZinkFinger\PWMS')
	print(len(pwmsnamen))
	pwmsnamen.sort()
	verzeichnispfadlist = os.listdir(verzeichnispfad)
	for datei in verzeichnispfadlist:
		if ('prediction' in datei):
			if os.path.exists(verzeichnispfad+'\\'+datei+'\\pdfs') == False:
				os.makedirs(verzeichnispfad+'\\'+datei+'\\pdfs')
			prediction = os.listdir(verzeichnispfad+'\\'+datei)
			preds = np.load(verzeichnispfad+'\\'+datei+'\\pwms.npy', 'r')
			kl_div = open('D:\Masterarbeit\ZinkFinger\Predictions\\'+datei+'\\kl_divergencen.tsv')
			kl_divZ = kl_div.readlines()
			i=0
			zaehler = 0
			for file in pwmsnamen:
				ausgabe = open(verzeichnispfad+'\\'+datei+'\\'+file, 'w')
				ausgabe.write('>'+file.split('.')[0]+'.'+file.split('.')[1]+'\n')#

				#Finde Länge der ursprunglichen PWM
				altpwm = open('D:\Masterarbeit\ZinkFinger\PWMS\\'+file)
				altpwmZ = altpwm.readlines()
				#print(file)
				#print(kl_divZ[zaehler].split('\t'))
				#print(len(preds[i,:]))

				if int(kl_divZ[zaehler].split('\t')[2]) == -1:
				#	print(preds[i,:])
					predswrite = np.flip(preds[i,:])
				else:
					predswrite = preds[i,:]
				start = int(kl_divZ[i].split('\t')[1])
				"""
				if int(kl_divZ[i].split('\t')[1])%4==0:
					print(file)
					start = int(kl_divZ[i].split('\t')[1])
				elif int(kl_divZ[i].split('\t')[1])%4==1:
					print('1')
					start = int(kl_divZ[i].split('\t')[1]) - 1
				elif int(kl_divZ[i].split('\t')[1])%4==2:
					print('2')
					start = int(kl_divZ[i].split('\t')[1]) - 2
				else:
					print('3')
					start = int(kl_divZ[i].split('\t')[1]) - 3
				"""
				k = 0
				if 0==0:
					#for j in range(start, start+(int(len(altpwmZ)-1)*4)):
					for j in range(start, start+160):
						ausgabe.write(str(predswrite[j]))
						if (k==3):
							ausgabe.write('\n')
						elif (k>3) & ((k-3)%4==0):
							ausgabe.write('\n')
						else:
							ausgabe.write('\t')
						k = k + 1
					i = i +1
				"""
				else:
					for j in range(start, int(kl_divZ[zaehler].split('\t')[1])+(int(len(altpwmZ)-1)*4)+2):
						ausgabe.write(str(predswrite[j]))
						if (k==3):
							ausgabe.write('\n')
						elif (k>3) & ((k-3)%4==0):
							ausgabe.write('\n')
						else:
							ausgabe.write('\t')
						k = k + 1
					i = i +1
				zaehler = zaehler + 1
				"""
def auswertunggegenliste():
	pfadpredpwms = os.listdir('D:\Masterarbeit\ZinkFinger\Predictions')
	for datei in pfadpredpwms:
		if ('prediction' in datei):
			print('Fall1')
			tsvdateimitdivergencen = open('D:\Masterarbeit\ZinkFinger\Predictions'+'\\'+datei+'\kl_divergencen.tsv')
			tsvdateimitdivergencenZ = tsvdateimitdivergencen.readlines()
			tsvgegenliste = open('D:\Masterarbeit\ZinkFinger\Predictions'+'\\'+datei+'\kl_divergencenGegenlist.tsv', 'w')
			tsvgegenliste.write('Index'+'\t'+'kl_div'+'\t'+'startpunkt'+'\t'+'normal_oder_reverse'+'\n')
			gegenliste = np.load('D:\Masterarbeit\ZinkFinger\zufallsliste2\\gegenneuzufallsliste_neu'+str(datei.split('_')[2])+'.npy')
			for i in range(0, len(gegenliste)):
				tsvgegenliste.write(str(gegenliste[i])+'\t')
				tsvgegenliste.write(tsvdateimitdivergencenZ[gegenliste[i]])
			"""
			if (int(datei.split('_')[0].split('n')[1]) < 11):
				print('Fall1')
				tsvdateimitdivergencen = open('D:\Masterarbeit\ZinkFinger\Predictions'+'\\'+datei+'\kl_divergencen.tsv')
				tsvdateimitdivergencenZ = tsvdateimitdivergencen.readlines()
				tsvgegenliste = open('D:\Masterarbeit\ZinkFinger\Predictions'+'\\'+datei+'\kl_divergencenGegenlist.tsv', 'w')
				tsvgegenliste.write('Index'+'\t'+'kl_div'+'\t'+'startpunkt'+'\t'+'normal_oder_reverse'+'\n')
				gegenliste = np.load('D:\Masterarbeit\ZinkFinger\zufallsliste2\\gegenneuzufallsliste_neu'+str(datei.split('_')[2])+'.npy')
				for i in range(0, len(gegenliste)):
					tsvgegenliste.write(str(gegenliste[i])+'\t')
					tsvgegenliste.write(tsvdateimitdivergencenZ[gegenliste[i]])
			elif ((int(datei.split('_')[0].split('n')[1]) > 10) & (int(datei.split('_')[0].split('n')[1]) < 100)):
				tsvdateimitdivergencen = open('D:\Masterarbeit\ZinkFinger\Predictions'+'\\'+datei+'\kl_divergencen.tsv')
				tsvdateimitdivergencenZ = tsvdateimitdivergencen.readlines()
				tsvgegenliste = open('D:\Masterarbeit\ZinkFinger\Predictions'+'\\'+datei+'\kl_divergencenGegenlist.tsv', 'w')
				tsvgegenliste.write('Index'+'\t'+'kl_div'+'\t'+'startpunkt'+'\t'+'normal_oder_reverse'+'\n')
				gegenliste = np.load('D:\Masterarbeit\ZinkFinger\zufallsliste3\\gegenneuzufallsliste_neu'+str(datei.split('_')[2])+'.npy')
				for i in range(0, len(gegenliste)):
					tsvgegenliste.write(str(gegenliste[i])+'\t')
					tsvgegenliste.write(tsvdateimitdivergencenZ[gegenliste[i]])
			else:
				print('2er runde')
				tsvdateimitdivergencen = open('D:\Masterarbeit\ZinkFinger\Predictions'+'\\'+datei+'\kl_divergencen.tsv')
				tsvdateimitdivergencenZ = tsvdateimitdivergencen.readlines()
				tsvgegenliste = open('D:\Masterarbeit\ZinkFinger\Predictions'+'\\'+datei+'\kl_divergencenGegenlist.tsv', 'w')
				tsvgegenliste.write('Index'+'\t'+'kl_div'+'\t'+'startpunkt'+'\t'+'normal_oder_reverse'+'\n')
				gegenliste = np.load('D:\Masterarbeit\ZinkFinger\zufallsliste2\\gegenneuzufallsliste_neu'+str(datei.split('_')[2])+'.npy')
				for i in range(0, len(gegenliste)):
					tsvgegenliste.write(str(gegenliste[i])+'\t')
					tsvgegenliste.write(tsvdateimitdivergencenZ[gegenliste[i]])
			"""
			"""
			elif ((int(datei.split('_')[0].split('n')[1]) > 100) & (int(datei.split('_')[0].split('n')[1]) < 111)):
				tsvdateimitdivergencen = open('D:\Masterarbeit\ZinkFinger\Predictions'+'\\'+datei+'\kl_divergencen.tsv')
				tsvdateimitdivergencenZ = tsvdateimitdivergencen.readlines()
				tsvgegenliste = open('D:\Masterarbeit\ZinkFinger\Predictions'+'\\'+datei+'\kl_divergencenGegenlist.tsv', 'w')
				tsvgegenliste.write('Index'+'\t'+'kl_div'+'\t'+'startpunkt'+'\t'+'normal_oder_reverse'+'\n')
				gegenliste = np.load('D:\Masterarbeit\ZinkFinger\zufallsliste2\\gegenneuzufallsliste_neu'+str(datei.split('_')[2])+'.npy')
				for i in range(0, len(gegenliste)):
					tsvgegenliste.write(str(gegenliste[i])+'\t')
					tsvgegenliste.write(tsvdateimitdivergencenZ[gegenliste[i]])
			elif (int(datei.split('_')[0].split('n')[1]) > 110):
				print('Fall4')
				tsvdateimitdivergencen = open('D:\Masterarbeit\ZinkFinger\Predictions'+'\\'+datei+'\kl_divergencen.tsv')
				tsvdateimitdivergencenZ = tsvdateimitdivergencen.readlines()
				tsvgegenliste = open('D:\Masterarbeit\ZinkFinger\Predictions'+'\\'+datei+'\kl_divergencenGegenlist.tsv', 'w')
				tsvgegenliste.write('Index'+'\t'+'kl_div'+'\t'+'startpunkt'+'\t'+'normal_oder_reverse'+'\n')
				gegenliste = np.load('D:\Masterarbeit\ZinkFinger\zufallsliste3\\gegenneuzufallsliste_neu'+str(datei.split('_')[2])+'.npy')
				for i in range(0, len(gegenliste)):
					tsvgegenliste.write(str(gegenliste[i])+'\t')
					tsvgegenliste.write(tsvdateimitdivergencenZ[gegenliste[i]])
			"""
def Auswertung_KL_DIV():
	pfadpredpwms = os.listdir('D:\Masterarbeit\ZinkFinger\Predictions')
	for datei in pfadpredpwms:
		if ('prediction' in datei):
			tsvdateimitdivergencen = open('D:\Masterarbeit\ZinkFinger\Predictions'+'\\'+datei+'\kl_divergencen.tsv')
			tsvdateimitdivergencenZ = tsvdateimitdivergencen.readlines()
			tsvgegenliste = open('D:\Masterarbeit\ZinkFinger\Predictions'+'\\'+datei+'\kl_divergencenGegenlist.tsv')
			tsvgegenlisteZ = tsvgegenliste.readlines()
			DurchschnittKLDIV = open('D:\Masterarbeit\ZinkFinger\Predictions'+'\\'+datei+'\kl_div_durchschnitt.tsv', 'w')
			MedianKLDIV = open('D:\Masterarbeit\ZinkFinger\Predictions'+'\\'+datei+'\kl_div_median.tsv', 'w')
			#ALLE
			median = []
			durchschnitt = 0
			for i in range(0, len(tsvdateimitdivergencenZ)):
				median.append(float(tsvdateimitdivergencenZ[i].split('\t')[0]))
				durchschnitt = durchschnitt + float(tsvdateimitdivergencenZ[i].split('\t')[0])
			durchschnitt = durchschnitt / len(tsvdateimitdivergencenZ)
			DurchschnittKLDIV.write('ALLE DURCHSCHNITT: '+str(durchschnitt)+'\n')
			median.sort()
			MedianKLDIV.write('ALLE MEDIAN: '+str(median[int(len(tsvdateimitdivergencenZ)/2)])+'\n')

			#GEGEN
			median = []
			durchschnitt = 0
			for i in range(1, len(tsvgegenlisteZ)):
				median.append(float(tsvgegenlisteZ[i].split('\t')[1]))
				durchschnitt = durchschnitt + float(tsvgegenlisteZ[i].split('\t')[1])
			durchschnitt = durchschnitt / len(tsvgegenlisteZ)
			DurchschnittKLDIV.write('TEST-SPLIT DURCHSCHNITT: '+str(durchschnitt))
			median.sort()
			MedianKLDIV.write('TEST-SPLIT MEDIAN: '+str(median[int(len(tsvgegenlisteZ)/2)]))

def findbestneuronalnetz():
	pfadpredpwms = os.listdir('D:\Masterarbeit\ZinkFinger\Predictions')
	output = open('D:\Masterarbeit\ZinkFinger\Predictions\\auswertung_kl_divergencen.tsv', 'w')
	for datei in pfadpredpwms:
		if ('prediction' in datei):
			MedianKLDIV = open('D:\Masterarbeit\ZinkFinger\Predictions'+'\\'+datei+'\kl_div_median.tsv')
			MedianKLDIVZ = MedianKLDIV.readlines()
			output.write(datei+'\n')
			output.write(MedianKLDIVZ[0])
			output.write(MedianKLDIVZ[1]+'\n')







#erzeugegegenteilliste2()
#erzeugegegenteilliste3()




KL_Div_ohne_Pwms_erzeugen()
SplitPredictionsInSinglePwmData()
auswertunggegenliste()
Auswertung_KL_DIV()

findbestneuronalnetz()
