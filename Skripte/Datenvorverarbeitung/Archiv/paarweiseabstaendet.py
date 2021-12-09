import numpy as np
import tensorflow as tf
from numpy import genfromtxt
from numpy import savetxt
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Activation, Dropout, Conv1D, Flatten, GlobalMaxPooling1D, GlobalAveragePooling1D,Reshape, LSTM, Input
import sys
import os
from sklearn.metrics import roc_auc_score,accuracy_score
from sklearn.model_selection import StratifiedKFold
from tensorflow.keras.models import clone_model
from tensorflow.python.ops import nn
from tensorflow.python.keras import backend
import tensorflow.keras.backend as K
from tensorflow.python.framework import ops
from tensorflow.python.ops import math_ops
from random import sample
from random import random
from numpy.random import default_rng
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import concatenate
from sklearn.preprocessing import normalize


def erzeugearr(x):
    arr = []
    arr.append(0)
    minus = x.shape[1]
    for i in range(0, int(x.shape[1]/27)):
        minus = minus-27
        arr.append(x.shape[1]-minus)
    return arr
def AbstandsMatrix():


    #Lese Blosum Matrix als Dict
    matrixFile = open('D:\Masterarbeit\Daten\\blosummatrix.txt')
    lines = matrixFile.readlines()
    matrixFile.close()
    dictaa = {}
    aminoacidstring = lines[0]
    aminoacidstring = aminoacidstring.split()
    i = 1
    while i <= (len(lines)-1):
        row = lines[i]
        row = row.split()

        j = 1
        for character in row[1:25]:
            dictaa[aminoacidstring[i-1],aminoacidstring[j-1]] = character # i,j changes (row, column) to (aa at row, aa at column) for keys
            j+=1
        i+=1
    #Füge Blosum Score in Meine Matrix ein
    #ERSTELLE MATRIX ÜBER ALLE 27-KOMBINATIONEN
    abc = '-ARNDCQEGHILKMFPSTWYVUOBZX*'
    code = {}
    for i in range(0, len(abc)):
        for j in range(0, len(abc)):
            if ((abc[i],abc[j]) in dictaa.keys()):
                code[abc[i], abc[j]] = dictaa[abc[i], abc[j]]
            else:
                code[abc[i], abc[j]] = 0
    return code
def MergeAlignmentsPwmZuordnungWeightsAbst(data,y,z):
	#ALLE
	pwmsgruppen = os.listdir('D:\Masterarbeit\Daten\PWMS_Nach_Gruppen_ueberarbeitet')
	alignments = os.listdir('D:\Masterarbeit\Daten\Alignments_onehot_ueberarbeitet')
	representativliste = os.listdir('D:\Masterarbeit\Daten\Cluster_Homeodomain\Motifs_representative')
	alignments.sort()
	abstand = np.zeros((data.shape[0],1))
	for index in range(0, data.shape[0]):
		index2 = alignments.index(representativliste[np.argmax(data[index,(6804+176):(6804+176+51)])+1].split('_')[2]+'_2.00.aln')
		abc = '-ARNDCQEGHILKMFPSTWYVUOBZX*'
		for k in range(1, len(y)):
			abstand[index,0] = abstand[index,0] + int(z[abc[np.argmax(data[index,y[k-1]:y[k]])],abc[np.argmax(data[index2,y[k-1]:y[k]])]])
	myarray = np.append(data, abstand, axis =1)
	np.save('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights_Abst.npy', myarray)
def MergeAlignmentsPwmZuordnungWeightsAbstGruppe(data,y,z):
	#ALLE
	pwmsgruppen = os.listdir('D:\Masterarbeit\Daten\PWMS_Nach_Gruppen_ueberarbeitet')
	alignments = os.listdir('D:\Masterarbeit\Daten\Alignments_onehot_ueberarbeitet')
	representativliste = os.listdir('D:\Masterarbeit\Daten\Cluster_Homeodomain\Motifs_representative')
	alignments.sort()
	abstand = np.zeros((data.shape[0],1))
	for index in range(0, data.shape[0]):
		index2 = alignments.index(representativliste[np.argmax(data[index,(6804+140):(6804+140+51)])+1].split('_')[2]+'_2.00.aln')
		abc = '-ARNDCQEGHILKMFPSTWYVUOBZX*'
		for k in range(1, len(y)):
			abstand[index,0] = abstand[index,0] + int(z[abc[np.argmax(data[index,y[k-1]:y[k]])],abc[np.argmax(data[index2,y[k-1]:y[k]])]])
	myarray = np.append(data, abstand, axis =1)
	np.save('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMsGruppen_Zuordnung_Weights_Abst.npy', myarray)

def normalisiereA():
	data = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights_Abst.npy')
	max = np.zeros((1,51))
	for index in range(0, data.shape[0]):
		if data[index,(6804+176+51+1):(6804+176+51+2)] > max[0,np.argmax(data[index,(6804+176):(6804+176+51)])]:
			max[0,np.argmax(data[index,(6804+176):(6804+176+51)])] = data[index,(6804+176+51+1):(6804+176+51+2)]
	for index in range(0, data.shape[0]):
		data[index,7032] = data[index,7032]/max[0,np.argmax(data[index,(6804+176):(6804+176+51)])]
	np.save('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights_Abst.npy', data)
def normalisiereG():
	data = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMsGruppen_Zuordnung_Weights_Abst.npy')
	max = np.zeros((1,51))
	for index in range(0, data.shape[0]):
		if data[index,(6804+140+51+1):(6804+140+51+2)] > max[0,np.argmax(data[index,(6804+140):(6804+140+51)])]:
			max[0,np.argmax(data[index,(6804+140):(6804+140+51)])] = data[index,(6804+140+51+1):(6804+140+51+2)]
	for index in range(0, data.shape[0]):
		data[index,6996] = data[index,6996]/max[0,np.argmax(data[index,(6804+140):(6804+140+51)])]
	np.save('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMsGruppen_Zuordnung_Weights_Abst.npy', data)


data = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights.npy', 'r')
data = data[:,0:6804]
data2 = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights.npy', 'r')

AbsMatrix = AbstandsMatrix()
MergeAlignmentsPwmZuordnungWeightsAbst(data2, erzeugearr(data), AbsMatrix)
data3 = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMsGruppen_Zuordnung_Weights.npy', 'r')
MergeAlignmentsPwmZuordnungWeightsAbstGruppe(data3, erzeugearr(data3), AbsMatrix)
normalisiereA()
normalisiereG()
