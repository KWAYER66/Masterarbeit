import os, sys
import numpy as np
from numpy import genfromtxt
from numpy import savetxt

#Functionen - Name ist Programm

# Diese Function -> ALTER STAND! <- Fülle PWMS anhand der Liste des Java Programms auf, sodass alle PWMS die gleiche Laenge haben
def FuellePWMsAufGleicheLaenge():
	OrdnerAllePWMS = os.listdir('/Users/kway/Desktop/Masterarbeit/PWMs_Homeodomain/Ausgabe_Aufgefuellte_PWMS/')
	if os.path.exists('/Users/kway/Desktop/Masterarbeit/PWMs_Homeodomain/Vergleich_PWMS') == False:
		os.makedirs('/Users/kway/Desktop/Masterarbeit/PWMs_Homeodomain/Vergleich_PWMS')

	#Öffne Die Ordner der beiden Gruppen
	#gruppe1 = sys.argv[1]

	laengepwm = 0
	for file in OrdnerAllePWMS:
		if 'shift' in file:
			pwmgruppe = os.listdir('/Users/kway/Desktop/Masterarbeit/PWMs_Homeodomain/Ausgabe_Aufgefuellte_PWMS/'+file)
			pwm = open('/Users/kway/Desktop/Masterarbeit/PWMs_Homeodomain/Ausgabe_Aufgefuellte_PWMS/'+file+'/'+pwmgruppe[0])
			pwmZ = pwm.readlines()
			if len(pwmZ) > laengepwm:
				laengepwm = len(pwmZ)
			pwm.close()

	for file in OrdnerAllePWMS:
		if 'shift' in file:
			pwmgruppe = os.listdir('/Users/kway/Desktop/Masterarbeit/PWMs_Homeodomain/Ausgabe_Aufgefuellte_PWMS/'+file)
			if os.path.exists('/Users/kway/Desktop/Masterarbeit/PWMs_Homeodomain/Vergleich_PWMS/'+file) == False:
				os.makedirs('/Users/kway/Desktop/Masterarbeit/PWMs_Homeodomain/Vergleich_PWMS/'+file)
			for file2 in pwmgruppe:
				if 'pwm' in file2:
					pwm = open('/Users/kway/Desktop/Masterarbeit/PWMs_Homeodomain/Ausgabe_Aufgefuellte_PWMS/'+file+'/'+ file2)
					pwmZ = pwm.readlines()
					laenge = (laengepwm-len(pwmZ))
					#Gerade
					if(laenge % 2) == 0:
						neuepwm= open('/Users/kway/Desktop/Masterarbeit/PWMs_Homeodomain/Vergleich_PWMS/'+file+'/'+file2, 'w')
						neuepwm.write('>'+file2+'\n')
						for i in range(0,int(laenge/2)):
							neuepwm.write('0,25\t0,25\t0,25\t0,25\n')
						for i in range(1,len(pwmZ)):
							neuepwm.write(pwmZ[i])
						for i in range(0,int(laenge/2)):
							neuepwm.write('0,25\t0,25\t0,25\t0,25\n')
					#ungerade
					if(laenge % 2) != 0:
						neuepwm= open('/Users/kway/Desktop/Masterarbeit/PWMs_Homeodomain/Vergleich_PWMS/'+file+'/'+file2, 'w')
						neuepwm.write('>'+file2+'\n')
						for i in range(0,int(laenge/2+0.5)):
							neuepwm.write('0,25\t0,25\t0,25\t0,25\n')
						for i in range(1,len(pwmZ)):
							neuepwm.write(pwmZ[i])
						for i in range(0,int(laenge/2-0.5)):
							neuepwm.write('0,25\t0,25\t0,25\t0,25\n')
#Entferne alle Kommas und ersetze diese durch Punkte
def pwmkommainpunkte():
	pwms = os.listdir('D:\Masterarbeit\Daten\PWM_shifts_full')
	if os.path.exists('D:\Masterarbeit\Daten\PWM_shifts_full_ueberarbeitet') == False:
		os.makedirs('D:\Masterarbeit\Daten\PWM_shifts_full_ueberarbeitet')

	for file in pwms:
		if 'pwm' in file:
			pwm = open('D:\Masterarbeit\Daten\PWM_shifts_full\\' + file)
			ausgabe = open('D:\Masterarbeit\Daten\PWM_shifts_full_ueberarbeitet\\' + file,'w')
			pwmZ = pwm.readlines()
			ausgabe.write('>'+file.split('.')[0]+'.'+file.split('.')[1]+'\n')
			pwmlist =[]
			for i in range(1,len(pwmZ)):
				for j in range(0,4):
					pwmlist.append(float(pwmZ[i].split('\n')[0].split('\t')[j].replace(',','.')))
			mypwm = np.asarray(pwmlist)[np.newaxis]
			for i in range(0, mypwm.shape[1]):
				ausgabe.write(str(mypwm[0][i]))
				if (i==3):
					ausgabe.write('\n')
				elif (i>3) & ((i-3)%4==0):
					ausgabe.write('\n')
				else:
					ausgabe.write('\t')

	pwms = os.listdir('D:\Masterarbeit\Daten\PWMS_Nach_Gruppen')
	if os.path.exists('D:\Masterarbeit\Daten\PWMS_Nach_Gruppen_ueberarbeitet') == False:
		os.makedirs('D:\Masterarbeit\Daten\PWMS_Nach_Gruppen_ueberarbeitet')

	for file in pwms:
		tf_gruppe = os.listdir('D:\Masterarbeit\Daten\PWMS_Nach_Gruppen\\'+file)
		if os.path.exists('D:\Masterarbeit\Daten\PWMS_Nach_Gruppen_ueberarbeitet\\'+file) == False:
			os.makedirs('D:\Masterarbeit\Daten\PWMS_Nach_Gruppen_ueberarbeitet\\'+file)

		for file2 in tf_gruppe:
			if 'pwm' in file2:
				pwm = open('D:\Masterarbeit\Daten\PWMS_Nach_Gruppen\\'+file+'\\'+file2)
				ausgabe = open('D:\Masterarbeit\Daten\PWMS_Nach_Gruppen_ueberarbeitet\\'+file+'\\'+file2,'w')
				pwmZ = pwm.readlines()
				ausgabe.write('>'+file2.split('.')[0]+'.'+file2.split('.')[1]+'\n')
				pwmlist =[]
				for i in range(1,len(pwmZ)):
					for j in range(0,4):
						pwmlist.append(float(pwmZ[i].split('\n')[0].split('\t')[j].replace(',','.')))
				mypwm = np.asarray(pwmlist)[np.newaxis]
				for i in range(0, mypwm.shape[1]):
					ausgabe.write(str(mypwm[0][i]))
					if (i==3):
						ausgabe.write('\n')
					elif (i>3) & ((i-3)%4==0):
						ausgabe.write('\n')
					else:
						ausgabe.write('\t')
#Erstelle Liste ALLE Zusammen in PWMS_Nach_Gruppen_ueberarbeitet
def ErstelleListPwmGruppe():
	pwmverzeichnis = os.listdir('D:\Masterarbeit\Daten\PWMS_Nach_Gruppen_ueberarbeitet')
	if os.path.exists('D:\Masterarbeit\Daten\PWMS_Nach_Gruppen_ueberarbeitet\AlleZusammen') == False:
		os.makedirs('D:\Masterarbeit\Daten\PWMS_Nach_Gruppen_ueberarbeitet\AlleZusammen')
	for datei in pwmverzeichnis:
	    if 'PWM' in datei:
	        pwmshifttf = os.listdir('D:\Masterarbeit\Daten\PWMS_Nach_Gruppen_ueberarbeitet\\'+datei)
	        for file in pwmshifttf:
	            pwm = open('D:\Masterarbeit\Daten\PWMS_Nach_Gruppen_ueberarbeitet\\'+datei+'\\'+file, 'r')
	            neuepwm = open('D:\Masterarbeit\Daten\PWMS_Nach_Gruppen_ueberarbeitet\AlleZusammen\\'+file, 'w')
	            pwmZ = pwm.readlines()
	            for i in range(0,len(pwmZ)):
	                neuepwm.write(pwmZ[i])
#Merge von Alignmentonehot-Codierung, PWM, Gruppen-Zugehörigkeit, Weights -> Input für NeuronalesNetz
def MergeAlignmentsPwmZuordnungWeights():
	#ALLE
	pwmsgruppen = os.listdir('D:\Masterarbeit\Daten\PWMS_Nach_Gruppen_ueberarbeitet')
	alignments = os.listdir('D:\Masterarbeit\Daten\Alignments_onehot_ueberarbeitet')

	arr = np.empty((0,6804+176+51+1),float)
	Zuordnung = dict(zip(pwmsgruppen, range(0,51)))
	alignments.sort()
	#Zuerst schreiben wir die Alignmentonehot in data
	for file in alignments:
		if ('aln' in file):
			zuarr = np.zeros((1,51))
			weightarr = np.zeros((1,1))
			#Lese Alignment ein
			alignment = open('D:\Masterarbeit\Daten\Alignments_onehot_ueberarbeitet\\' + file)
			alignmentZeile = alignment.readlines()
			data = []
			for i in range(0,len(alignmentZeile)):
					data.append(int(float(alignmentZeile[i].split('\n')[0])))
			myarray = np.asarray(data)[np.newaxis]

			#Berechne Zuordnungen zu den TF-Gruppen
			for file2 in pwmsgruppen:
				pwmgruppe = os.listdir('D:\Masterarbeit\Daten\PWMS_Nach_Gruppen_ueberarbeitet\\'+file2)
				for i in range(0,len(pwmgruppe)):
					if file.split('.')[0] == pwmgruppe[i].split('.')[0]:
						zuarr[0,Zuordnung[file2]] = 1

			#und jetzt hängen wir die pwms dran
			pwm = open('D:\Masterarbeit\Daten\PWM_shifts_full_ueberarbeitet\\' + file.split('.')[0] +'.00.pwm')
			pwmZ = pwm.readlines()
			pwmlist = []
			for i in range(1,len(pwmZ)):
				for j in range(0,4):
					pwmlist.append(float(pwmZ[i].split('\n')[0].split('\t')[j].replace(',','.')))
			mypwm = np.asarray(pwmlist)[np.newaxis]
			myarray = np.append(myarray, mypwm, axis =1)
			myarray = np.append(myarray,zuarr,axis = 1)

			#Repräsentaten
			representativliste = os.listdir('D:\Masterarbeit\Daten\Cluster_Homeodomain\Motifs_representative')
			for represent in representativliste:
				if 'TF' in represent:
					if file.split('.')[0] == represent.split('_')[2]+'_2':
						weightarr[0,0] = 1
			myarray = np.append(myarray,weightarr,axis = 1)
			arr = np.append(arr, myarray, axis =0)
	np.save('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights.npy', arr)

	#Das Gleiche Nochmal, koente auch in eine function?
	arr = np.empty((0,6804+140+51+1),float)
	alignments.sort()
	Zuordnung = dict(zip(pwmsgruppen, range(0,51)))
	#Zuerst schreiben wir die Alignmentonehot in data
	for file in alignments:
		if ('aln' in file):
			zuarr = np.zeros((1,51))
			weightarr = np.zeros((1,1))
			#Lese Alignment ein
			alignment = open('D:\Masterarbeit\Daten\Alignments_onehot_ueberarbeitet\\' + file)
			alignmentZeile = alignment.readlines()
			data = []
			for i in range(0,len(alignmentZeile)):
					data.append(int(float(alignmentZeile[i].split('\n')[0])))
			myarray = np.asarray(data)[np.newaxis]

			#Zuordnung und PWM in data
			for file2 in pwmsgruppen:
				pwmgruppe = os.listdir('D:\Masterarbeit\Daten\PWMS_Nach_Gruppen_ueberarbeitet\\'+file2)
				for i in range(0,len(pwmgruppe)):
					if file.split('.')[0] == pwmgruppe[i].split('.')[0]:
						pwm = open('D:\Masterarbeit\Daten\PWMS_Nach_Gruppen_ueberarbeitet\\'+file2+'\\'+file.split('.')[0]+'.00.pwm')
						zuarr[0,Zuordnung[file2]]=1
						pwmZ = pwm.readlines()
						pwmlist = []
						for i in range(1,len(pwmZ)):
							for j in range(0,4):
								pwmlist.append(float(pwmZ[i].split('\n')[0].split('\t')[j].replace(',','.')))
						mypwm = np.asarray(pwmlist)[np.newaxis]
						myarray =np.append(myarray,mypwm,axis=1)
						myarray = np.append(myarray,zuarr,axis = 1)


			representativliste = os.listdir('D:\Masterarbeit\Daten\Cluster_Homeodomain\Motifs_representative')

			for represent in representativliste:
				if 'TF' in represent:
					if file.split('.')[0] == represent.split('_')[2]+'_2':
						weightarr[0,0] = 1
			myarray = np.append(myarray,weightarr,axis = 1)
			arr =np.append(arr,myarray,axis=0)



	np.save('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMsGruppen_Zuordnung_Weights.npy', arr)

ErstelleListPwmGruppe()
#MergeAlignmentsPwmZuordnungWeights()
