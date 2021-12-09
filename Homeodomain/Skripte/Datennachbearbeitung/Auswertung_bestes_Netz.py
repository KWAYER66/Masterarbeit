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

def takeSecond(elem):
	return elem[1]
def auswertung_in_list():
	pfadpredpwms = os.listdir('D:\Masterarbeit\Predictions')
	auswertungsdatei = open('D:\Masterarbeit\AuswertungNeuronaleNetze.tsv','w')
	list = []
	for datei in pfadpredpwms:
		dl_kl_gegen = open('D:\Masterarbeit\Predictions\\'+datei+'\\Durchschnitt_kl_divergencenGegenListe.tsv')
		dl_kl_gegenZ = dl_kl_gegen.readlines()
		list.append((datei, float(dl_kl_gegenZ[0])))
	list.sort(key = takeSecond)
	for element in list:
		auswertungsdatei.write(str(element[0])+'\t'+str(element[1])+'\n')


auswertung_in_list()
