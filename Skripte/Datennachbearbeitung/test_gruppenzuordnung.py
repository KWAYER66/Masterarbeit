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

def testgruppenzuordnung():
    predictionverzeichnis = os.listdir('D:\Masterarbeit\Predictions')
    data = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights_Abst_tf.npy')[:,(6804+176):(6804+176+51)]
    for predictionordner in predictionverzeichnis:
        if 'prediction' in predictionordner:
            predictionordnerverzeichnis = os.listdir('D:\Masterarbeit\Predictions\\'+predictionordner)
            for file in predictionordnerverzeichnis:
                if 'zuordnung' in file:

                    ausgabezuordnung = open('D:\Masterarbeit\Predictions\\'+predictionordner+'\\zuordnungplotdaten.tsv','w')
                    #testlist = np.load('D:\Masterarbeit\Daten\Liste_Train_Test_Split\gegenzufallsliste'+str(predictionordner.split('_')[4])+'.npy')
                    #traininglist = np.load('D:\Masterarbeit\Daten\Liste_Train_Test_Split\zufallsliste'+str(predictionordner.split('_')[4])+'.npy')
                    zuordnungsfile = np.load('D:\Masterarbeit\Predictions\\'+predictionordner+'\\'+file)
                    for i in range(0, zuordnungsfile.shape[0]):
                        ausgabezuordnung.write(str(np.argmax(data[i,:]))+'\t')
                        ausgabezuordnung.write(str(np.argmax(zuordnungsfile[i,:]))+'\n')

testgruppenzuordnung()
