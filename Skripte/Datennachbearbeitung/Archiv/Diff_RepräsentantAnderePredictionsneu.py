import numpy as np
from numpy import genfromtxt
from numpy import savetxt
import sys
import os

def erstelledatei():
    pwmgruppen = os.listdir('D:\Masterarbeit\Daten\PWM_shifts_full_ueberarbeitet')
    ausgabe = open('D:\Masterarbeit\RepresentantenandIndexneu.tsv','w')
    myarr = []
    #1. Finde Representanten
    for pwm in pwmgruppen:
        print(pwm)
        representativliste = os.listdir('D:\Masterarbeit\DBDs')
        for potentiellrepresentant in representativliste:
            if 'ergebnis' in potentiellrepresentant:
                representanttfaktor = os.listdir('D:\Masterarbeit\DBDs\\'+potentiellrepresentant)
                if len(representanttfaktor) != 0:
                    represente = os.listdir('D:\Masterarbeit\DBDs\\'+potentiellrepresentant+'\\Motifs_representative')
                    for represent in represente:
                        if 'TF' in represent:
                            if pwm.split('.')[0] == represent.split('_')[2]+'_2':
                                ausgabe.write(pwm+'\t')
                                ausgabe.write(str(pwmgruppen.index(pwm))+'\n')
                                myarr.append(pwmgruppen.index(pwm))
                else:
                    ausgabe.write(pwm+'\t')
                    ausgabe.write(str(pwmgruppen.index(pwm))+'\n')
                    myarr.append(pwmgruppen.index(pwm))

    arr = np.array(myarr)
    np.save('D:\Masterarbeit\RepresentantenIndexneu.npy', arr)

def test():
    indices = np.load('D:\Masterarbeit\RepresentantenIndex.npy')
    predictions = os.listdir('D:\Masterarbeit\Predictions')
    for prediction in predictions:
        if 'prediction' in prediction:
            ausgaberepresentanten = open('D:\Masterarbeit\Predictions\\'+prediction+'\kl_divergencenrepresentanten.tsv','w')
            ausgabeandere = open('D:\Masterarbeit\Predictions\\'+prediction+'\kl_divergencenandere.tsv','w')
            kl_div = open('D:\Masterarbeit\Predictions\\'+prediction+'\kl_divergencen2.tsv')
            kl_divZ = kl_div.readlines()

            for i in range(0, len(kl_divZ)):
                nix = 0
                for j in range(0, indices.shape[1]):
                    #1. Fall schreibe kl div für representaten
                    if i == int(indices[0,j]):
                        ausgaberepresentanten.write(str(indices[0,j])+',')
                        ausgaberepresentanten.write(kl_divZ[i])
                        nix = 1
                if nix == 0:
                    ausgabeandere.write(kl_divZ[i])



#erstelledatei()
test()
#indices = np.load('D:\Masterarbeit\RepresentantenIndex.npy')
#print(indices)
