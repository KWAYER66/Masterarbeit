import numpy as np
from numpy import genfromtxt
from numpy import savetxt
import sys
import os

def erstelledatei():
    representativliste = os.listdir('D:\Masterarbeit\Daten\Cluster_Homeodomain\Motifs_representative')
    ausgabe = open('D:\Masterarbeit\RepresentantenandIndex.tsv','w')
    myarr = np.zeros((1,51))
    pwmsalle = os.listdir('D:\Masterarbeit\Daten\PWM_shifts_full_ueberarbeitet')

    for representant in range(0,len(representativliste)):
        if 'TF_0' in representativliste[representant]:
            for pwm in pwmsalle:
                if representativliste[representant].split('_')[2] in pwm:
                    ausgabe.write(pwm+'\t')
                    ausgabe.write(str(pwmsalle.index(pwm))+'\n')
                    myarr[0,representant-1] = pwmsalle.index(pwm)
    np.save('D:\Masterarbeit\RepresentantenIndex.npy', myarr)
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
