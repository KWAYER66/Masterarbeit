import numpy as np
import tensorflow as tf
from numpy import genfromtxt
from numpy import savetxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout, Conv1D, Flatten, GlobalMaxPooling1D, GlobalAveragePooling1D,Reshape, LSTM
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
import io
from contextlib import redirect_stdout
from scipy.special import softmax

def normalisiere(x):
	y = x.reshape((int(x.shape[0]/4),4))
	for i in range(0, y.shape[0]):
		y[i,:] = y[i,:] / sum(y[i,:])
	return y.reshape((x.shape[0]))
def SplitPredictionsInSinglePwmDataPseudo():
	pwmsnamen = os.listdir('D:\Masterarbeit\Daten\PWM_shifts_full_ueberarbeitet')
	pwmsnamen.sort()

	data = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz2\AlignmentsPWMs_Zuordnung_Weights_Abst_tf.npy')[:,6804:6804+176]
	print(data[0,:])
	if os.path.exists('D:\Masterarbeit\Daten\Input_NeuronalesNetz2\pwms') == False:
		os.makedirs('D:\Masterarbeit\Daten\Input_NeuronalesNetz2\pwms')
	i=0
	for file in pwmsnamen:
		ausgabe = open('D:\Masterarbeit\Daten\Input_NeuronalesNetz2\pwms\\'+file, 'w')
		ausgabe.write('>'+file.split('.')[0]+'.'+file.split('.')[1]+'\n')
		for j in range(0, data.shape[1]):
			ausgabe.write(str(data[i][j]))
			if (j==3):
				ausgabe.write('\n')
			elif (j>3) & ((j-3)%4==0):
				ausgabe.write('\n')
			else:
				ausgabe.write('\t')
		i = i +1
def pseudocountsnpy():
	if os.path.exists('D:\Masterarbeit\Daten\Input_NeuronalesNetz2') == False:
		os.makedirs('D:\Masterarbeit\Daten\Input_NeuronalesNetz2')
	data = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights_Abst_tf.npy')
	data2 = data[:,6804:6804+176]+0.05
	for i in range(0, data2.shape[0]):
		data2[i,:] = normalisiere(data2[i,:])
	myarray = np.append(data[:,0:6804], data2, axis=1)
	myarray = np.append(myarray, data[:, 6804+176:data.shape[1]], axis=1)
	np.save('D:\Masterarbeit\Daten\Input_NeuronalesNetz2\AlignmentsPWMs_Zuordnung_Weights_Abst_tf.npy', myarray)
pseudocountsnpy()
SplitPredictionsInSinglePwmDataPseudo()
