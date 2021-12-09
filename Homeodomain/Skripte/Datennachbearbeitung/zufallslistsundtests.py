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

#sys.argv[1] = verzeichnispfad in dem die predictions sind
predpfad = sys.argv[1]
def erzeugezufallsliste():
  data = np.load('D:\Inferenz_von_TF_Bindepraeferenzen\AlignmentPWMBeide\AlignmentsPWMs.npy')
  rng = default_rng()
  liste1 = rng.choice(range(0,len(data)), size =1500, replace = False)
  np.save('D:\Inferenz_von_TF_Bindepraeferenzen\InputListe\zufallsliste.npy',liste1)
def schreibelisteintsv():
  liste = np.load('D:\Inferenz_von_TF_Bindepraeferenzen\InputListe\zufallsliste.npy')
  ausgabedata = open('D:\Inferenz_von_TF_Bindepraeferenzen\InputListe\zufallsliste.tsv','w')
  for i in range(0,len(liste)):
    ausgabedata.write(str(liste[i])+'\t')
def erzeugegegenteilliste():
  liste = np.load('D:\Inferenz_von_TF_Bindepraeferenzen\InputListe\zufallsliste.npy')
  liste =np.sort(liste)
  gegenliste = []
  zaehler = 0
  for i in range(0,liste.shape[0]):
    #print(liste[i])
    #print(zaehler)
    if zaehler == liste[i]:
      zaehler = zaehler +1
    elif zaehler != liste[i]:
      for j in range(0,liste[i]-zaehler):
        gegenliste.append(zaehler)
        zaehler = zaehler + 1
      zaehler = zaehler +1
    np.save('D:\Inferenz_von_TF_Bindepraeferenzen\InputListe\gegenzufallsliste.npy',gegenliste)
def auswertunggegenliste(x):
  liste = np.sort(np.load('D:\Inferenz_von_TF_Bindepraeferenzen\InputListe\gegenzufallsliste.npy'))
  predictionsneuronalenetze = os.listdir(x)
  for file in predictionsneuronalenetze:
    if 'npy' not in file:
      kl_div = open(x+'\\'+file+'\\kl_divergencen.tsv')
      kl_divGegen = open(x+'\\'+file+'\\kl_divergencenGegenListe.tsv', 'w')
      kl_divGegenPlot = open(x+'\\'+file+'\\kl_divergencenGegenListePlot.tsv', 'w')
      kl_divZ = kl_div.readlines()
      for i in range(0,len(kl_divZ)):
        for j in range(0, len(liste)):
          if i == liste[j]:
            kl_divGegen.write(kl_divZ[i])
            kl_divGegenPlot.write(kl_divZ[i].split('\t')[1])
def durchschnittkldiv(x):
  predictionsneuronalenetze = os.listdir(x)
  for file in predictionsneuronalenetze:
    if 'npy' not in file:
      divergencen = 0
      divergencenzaehler = 0
      durchschnittkl_divGegen = open(x+'\\'+file+'\\Durchschnitt_kl_divergencenGegenListe.tsv', 'w')
      kl_divGegen = open(x+'\\'+file+'\\kl_divergencenGegenListe.tsv')
      kl_divGegenZ = kl_divGegen.readlines()
      for i in range(0,len(kl_divGegenZ)):
        divergencen = divergencen + float(kl_divGegenZ[i].split('\t')[1])
        divergencenzaehler = divergencenzaehler + 1
      durchschnittkl_divGegen.write(str(divergencen/divergencenzaehler) +'\n')
      #durchschnittkl_divGegen.write('anzahl: '+ str(divergencenzaehler) +'\n')


#erzeugegegenteilliste()
auswertunggegenliste(predpfad)
durchschnittkldiv(predpfad)
