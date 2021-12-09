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


def kl_divergence_by_christian(y_true, y_pred):
  y_pred = ops.convert_to_tensor_v2_with_dispatch(y_pred)
  y_true = math_ops.cast(y_true, y_pred.dtype)
  y_true = backend.clip(y_true, backend.epsilon(), 1)
  y_pred = backend.clip(y_pred, backend.epsilon(), 1)
  return math_ops.reduce_sum(y_true * math_ops.log(y_true / y_pred), axis=-1)


#sys.argv[1] = verzeichnispfad in dem die predictions sind
pfadinputpwms = 'D:\Inferenz_von_TF_Bindepraeferenzen\PWM_shifts_full_korrekt'
pfadinputpwmsG = 'D:\Inferenz_von_TF_Bindepraeferenzen\PWMS_Nach_Gruppen_korrekt\AlleZusammen'
listpwmsnamen = os.listdir(pfadinputpwms)
listpwmsnamenG = os.listdir(pfadinputpwmsG)

pfadpredpwms = os.listdir(sys.argv[1])


for datei in pfadpredpwms:
	if ('predictions1' in datei) & ('176' in datei):
		if 'npy' not in datei:
			tsvdateimitdivergencen = open(sys.argv[1]+'\\'+datei+'\kl_divergencen.tsv','w')
			for file in listpwmsnamen:
				if 'pwm' in file:
					inputpwm = open(pfadinputpwms+"\\"+file)
					pwmZ = inputpwm.readlines()
					predpwm = open(sys.argv[1]+'\\'+datei+"\\"+file)
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
	elif ('predictions1' in datei) & ('140' in datei):
		if 'npy' not in datei:
			tsvdateimitdivergencen = open(sys.argv[1]+'\\'+datei+'\kl_divergencen.tsv','w')
			for file in listpwmsnamenG:
				if 'pwm' in file:
					inputpwm = open(pfadinputpwmsG+'\\'+file)
					pwmZ = inputpwm.readlines()
					predpwm = open(sys.argv[1]+'\\'+datei+"\\"+file)
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
