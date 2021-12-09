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

kl_divtest = np.ones(51)
kl_divtest = kl_divtest/51

data = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights_Abst_tf.npy')[:,(6804+176):(6804+176+51)]
maxabweichung = float(kl_divergence_by_christian(kl_divtest, data[0,:]).numpy())
print(maxabweichung)

predictionverzeichnis = os.listdir('D:\Masterarbeit\Predictions')
ausgabezuordnung = open('D:\Masterarbeit\Predictions\AuswertungZuordnungen.tsv','w')
ausgabezuordnung2 = open('D:\Masterarbeit\Predictions\AuswertungZuordnungendetail.tsv','w')
ausgabesicherheitalle = open('D:\Masterarbeit\Predictions\AuswertungSicherheitzuordnung.tsv','w')

for predictionordner in predictionverzeichnis:
    if 'prediction' in predictionordner:
        predictionordnerverzeichnis = os.listdir('D:\Masterarbeit\Predictions\\'+predictionordner)
        for file in predictionordnerverzeichnis:
            if 'zuordnung' in file:
                ausgabesicherheit = open('D:\Masterarbeit\Predictions\\'+predictionordner+'\\Sicherheitsmass.tsv','w')
                ausgabezuordnung.write(predictionordner+'\n')
                ausgabezuordnung2.write(predictionordner+'\n')
                ausgabesicherheitalle.write(predictionordner+'\n')
                ausgabesicherheit.write(predictionordner+'\n')
                testlist = np.load('D:\Masterarbeit\Daten\Liste_Train_Test_Split\gegenzufallsliste'+str(predictionordner.split('_')[4])+'.npy')
                traininglist = np.load('D:\Masterarbeit\Daten\Liste_Train_Test_Split\zufallsliste'+str(predictionordner.split('_')[4])+'.npy')
                zuordnungsfile = np.load('D:\Masterarbeit\Predictions\\'+predictionordner+'\\'+file)
                #1. Bestimme Sicherheitsmaß für alle
                ausgabesicherheit.write('Alle: \n')
                ausgabesicherheitalle.write('Alle: \n')
                sicherheit = 0
                for i in range(0, 10):
                    zebra = maxabweichung - float(kl_divergence_by_christian(kl_divtest, zuordnungsfile[i,:]).numpy())
                    zebra = zebra / maxabweichung
                    ausgabesicherheit.write(str(zebra)+'\n')
                    sicherheit = sicherheit + zebra
                sicherheit = sicherheit / int(zuordnungsfile.shape[0])
                ausgabesicherheitalle.write(str(sicherheit)+'\n')
                #1. Bestimme Sicherheitsmaß für TestData
                zuordnungsfile2 = zuordnungsfile[testlist,:]
                data2 = data[testlist,:]
                ausgabesicherheit.write('Testdata: \n')
                ausgabesicherheitalle.write('Testdata: \n')
                sicherheit = 0
                print(zuordnungsfile2.shape[0])
                for i in range(0, zuordnungsfile2.shape[0]):
                    ausgabesicherheit.write(str(maxabweichung - float(kl_divergence_by_christian(kl_divtest,zuordnungsfile2[i,:]).numpy())/maxabweichung)+'\n')
                    sicherheit = sicherheit + (maxabweichung - float(kl_divergence_by_christian(kl_divtest, zuordnungsfile[i,:]).numpy()))/maxabweichung
                sicherheit = sicherheit / int(zuordnungsfile2.shape[0])
                ausgabesicherheitalle.write(str(sicherheit)+'\n')


                #2. Bestimme Abweichung zur tatsächlichen Zuordnung von allen

                anzahlrichtige = 0
                anzahlfalsche = 0
                #ausgabezuordnung2.write('falsche-ids:\n')

                for i in range(0, zuordnungsfile.shape[0]):
                    if np.argmax(zuordnungsfile[i,:]) == np.argmax(data[i,:]):
                        anzahlrichtige = anzahlrichtige + 1
                    else:
                        anzahlfalsche = anzahlfalsche + 1
                        #ausgabezuordnung2.write(i+'\n')
                ausgabezuordnung.write('anzahlrichtige:')
                ausgabezuordnung.write(str(anzahlrichtige)+'\n')
                ausgabezuordnung.write('anzahlfalsche:')
                ausgabezuordnung.write(str(anzahlfalsche)+'\n')
                #2. Bestimme Abweichung zur tatsächlichen Zuordnung von Testdaten
                ausgabezuordnung.write('Testdata\n')
                ausgabezuordnung2.write('Testdata\n')
                anzahlrichtige = 0
                anzahlfalsche = 0
                ausgabezuordnung2.write('falsche-ids:\n')
                zuordnungsfile2 = zuordnungsfile[testlist,:]
                data2 = data[testlist,:]
                for i in range(0, zuordnungsfile2.shape[0]):
                    if np.argmax(zuordnungsfile2[i,:]) == np.argmax(data2[i,:]):
                        anzahlrichtige = anzahlrichtige + 1
                    else:
                        anzahlfalsche = anzahlfalsche + 1
                        ausgabezuordnung2.write(str(i)+'\n')
                        #ausgabezuordnung2.write(str(zuordnungsfile[i,:])+'\n')
                ausgabezuordnung.write('anzahlrichtige:')
                ausgabezuordnung.write(str(anzahlrichtige)+'\n')
                ausgabezuordnung.write('anzahlfalsche:')
                ausgabezuordnung.write(str(anzahlfalsche)+'\n')
                #2. Bestimme Abweichung zur tatsächlichen Zuordnung von Trainingsdaten
                ausgabezuordnung.write('Trainingsdata\n')
                ausgabezuordnung2.write('Trainingsdata\n')
                anzahlrichtige = 0
                anzahlfalsche = 0
                ausgabezuordnung2.write('falsche-ids:\n')
                zuordnungsfile2 = zuordnungsfile[traininglist,:]
                data2 = data[traininglist,:]
                for i in range(0, zuordnungsfile2.shape[0]):
                    if np.argmax(zuordnungsfile2[i,:]) == np.argmax(data2[i,:]):
                        anzahlrichtige = anzahlrichtige + 1
                    else:
                        anzahlfalsche = anzahlfalsche + 1
                        ausgabezuordnung2.write(str(i)+'\n')
                        #ausgabezuordnung2.write(str(zuordnungsfile[i,:])+'\n')
                ausgabezuordnung.write('anzahlrichtige:')
                ausgabezuordnung.write(str(anzahlrichtige)+'\n')
                ausgabezuordnung.write('anzahlfalsche:')
                ausgabezuordnung.write(str(anzahlfalsche)+'\n')
