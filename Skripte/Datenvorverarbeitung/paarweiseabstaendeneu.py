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
	pwmsgruppen = os.listdir('D:\Masterarbeit\Daten\PWM_shifts_full_ueberarbeitet')
	pwmsgruppen.sort()
	abc = '-ARNDCQEGHILKMFPSTWYVUOBZX*'

	abstand = np.zeros((data.shape[0],data.shape[0]))
	#for index in range(0, data.shape[0]):
	for index in range(0, data.shape[0]):
		print(index)
		for index2 in range(0, data.shape[0]):
			for k in range(1,len(y)):
				abstand[index,index2] = abstand[index,index2] + int(z[abc[np.argmax(data[index,y[k-1]:y[k]])],abc[np.argmax(data[index2,y[k-1]:y[k]])]])
	myarray = np.append(data, abstand, axis =1)
	np.save('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights_Abst.npy', myarray)


data = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights.npy', 'r')
data = data[:,0:6804]
data2 = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights.npy', 'r')

AbsMatrix = AbstandsMatrix()
MergeAlignmentsPwmZuordnungWeightsAbst(data2, erzeugearr(data), AbsMatrix)
