import numpy as np
import os
pwmsgruppen = os.listdir('D:\Masterarbeit\Daten\PWM_shifts_full_ueberarbeitet')
data1 = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights_Abst.npy')
data2 = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMsGruppen_Zuordnung_Weights_Abst.npy')
faktortfneurinput = np.zeros((data1.shape[0],1))
#print(pwmsgruppen[1].split('.')[0]+'.'+pwmsgruppen[1].split('.')[1])
pwmallfile = open('D:\Masterarbeit\Daten\PWM.txt')
pwmallfileZ = pwmallfile.readlines()
dict_tffaktors = {}
tffaktorvorkommen = {}
for pwm in pwmsgruppen:
    zaehler = 0
    for i in range(0, len(pwmallfileZ)):
        if pwm.split('.')[0]+'.'+pwm.split('.')[1] in pwmallfileZ[i]:
            tffaktor = pwmallfileZ[i-3].split('\t')[1].splitlines()[0]
    for i in range(0, len(pwmallfileZ)):
        if tffaktor in pwmallfileZ[i]:
            #speicher in dict
            dict_tffaktors[pwmallfileZ[i+3].split('\t')[1].splitlines()[0]] = tffaktor

for k in range(0, len(pwmsgruppen)):
    pwm = pwmsgruppen[k]
    print(dict_tffaktors[pwm.split('.')[0]+'.'+pwm.split('.')[1]])
    faktortfneurinput[k,0] = sum(value == dict_tffaktors[pwm.split('.')[0]+'.'+pwm.split('.')[1]] for value in dict_tffaktors.values())

myarray = np.append(data1, faktortfneurinput, axis =1)
np.save('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights_Abst_tf.npy', myarray)
myarray = np.append(data2, faktortfneurinput, axis =1)
np.save('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMsGruppen_Zuordnung_Weights_Abst_tf.npy', myarray)
