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

testgruppenzuordnungtestdata()
