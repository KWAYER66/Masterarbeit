import sys, os
import gzip
import shutil
import numpy as np
from numpy import genfromtxt
from numpy.random import default_rng


def CreateFolder(Path):
	if os.path.exists(Path) == False:
		os.makedirs(Path)
def Punkt6_SplitMultiplesAlignment():
	CreateFolder('D:\Masterarbeit\ZinkFinger\AlignmentsZF_stockholm_verarbeitet')

	MultiplesAlignment = open('D:\Masterarbeit\ZinkFinger\MultiplesAlignment_Stockholm.out')
	MulitplesAlignmentZ = MultiplesAlignment.readlines()

	for zeile in range(2,len(MulitplesAlignmentZ)):
		if MulitplesAlignmentZ[zeile][0:1] == 'M':
			SepariertesFile = open('D:\Masterarbeit\ZinkFinger\AlignmentsZF_stockholm_verarbeitet\\'+MulitplesAlignmentZ[zeile].split(' ')[0]+'.aln', 'w')
			SepariertesFile.write('>'+MulitplesAlignmentZ[zeile].split(' ')[0]+'\n')
			SepariertesFile.write(MulitplesAlignmentZ[zeile].split(' ')[len(MulitplesAlignmentZ[zeile].split(' '))-1].split('\n')[0].replace(".","-").upper())
			#print(MulitplesAlignmentZ[zeile].split(' ')[len(MulitplesAlignmentZ[zeile].split(' '))-1].split('\n')[0].replace(".","-").upper())
def Punkt7_AlignmentsOnehot():
	alphabet = '-ARNDCQEGHILKMFPSTWYVUOBZX*'
	char_to_int = dict((c,k) for k, c in enumerate(alphabet))
	alignments = os.listdir('D:\Masterarbeit\ZinkFinger\AlignmentsZF_stockholm_verarbeitet')

	CreateFolder('D:\Masterarbeit\ZinkFinger\AlignmentsZF_stockholm_onehot')

	#Gehe alle Alignmentdateien durch
	for alignment in alignments:
		if ('aln' in alignment):
			alignmentfile = open('D:\Masterarbeit\ZinkFinger\AlignmentsZF_stockholm_verarbeitet\\'+alignment)
			alignmentfileZ = alignmentfile.readlines()

			alignmentfileNEW =  open('D:\Masterarbeit\ZinkFinger\AlignmentsZF_stockholm_onehot\\'+alignment, 'w')
			alignmentfileNEW.write(alignmentfileZ[0])

			#Gehe alle Zeilen der Alignmentdatei durch
			for i in range(1, len(alignmentfileZ)):

				integer_encoded = [char_to_int[char] for char in alignmentfileZ[i].split('\n')[0]]
				onehot_encoded = list()

				#Codiere Onehot und schreibe in neues AlignmentFile
				for value in integer_encoded:
					letter = [0 for _ in range(len(alphabet))]
					letter[value] = 1
					onehot_encoded.append(letter)

				for j in range(0, len(onehot_encoded)):
					alignmentfileNEW.write(str(onehot_encoded[j]).replace(',','').replace('[','').replace(']','').replace(' ',''))
def Punkt8_FuegeEinzelneAlignmentFilesJEWEILSZusammen():
	#Erstelle Order
	CreateFolder('D:\Masterarbeit\ZinkFinger\AlignmentsZF_onehot_stockholm_merge')
	#Liste AlignmentsOneHot
	AlignmentsFolderOneHot = os.listdir('D:\Masterarbeit\ZinkFinger\AlignmentsZF_stockholm_onehot')
	#Liste AlignmentsFolderVorher (Fuer die Namen)
	AlignmentsFolderVorher = os.listdir('D:\Masterarbeit\ZinkFinger\AlignmentsZFVorherOhneGAPS')

	#1. For Schleife - Gehe Alle Motiv-IDs durch
	for AlignmentsFileVorher in AlignmentsFolderVorher:
		#2. For Schleife - Finde Alle ZF-Module zur Motiv-ID
		for AlignmentsFileOneHot in AlignmentsFolderOneHot:
			if AlignmentsFileVorher.split('.')[0] in AlignmentsFileOneHot:

				#Oeffne OneHot File
				AlignmentsFileOneHotOffen = open('D:\Masterarbeit\ZinkFinger\AlignmentsZF_stockholm_onehot\\'+AlignmentsFileOneHot)
				AlignmentsFileOneHotOffenZ = AlignmentsFileOneHotOffen.readlines()
				#print(AlignmentsFileOneHotOffenZ[1])
				#print(int(AlignmentsFileOneHot.split('_')[2].split('.')[0]))

				#Pruefe ob MergeDatei schon existiert
				if int(AlignmentsFileOneHot.split('_')[2].split('.')[0]) == 0:
					AlignmentsFileMerge = open('D:\Masterarbeit\ZinkFinger\AlignmentsZF_onehot_stockholm_merge\\'+AlignmentsFileVorher.split('.')[0]+'.00.aln', 'w')

					AlignmentsFileMerge.write(AlignmentsFileOneHotOffenZ[0])
					AlignmentsFileMerge.write(AlignmentsFileOneHotOffenZ[1])
				else:
					AlignmentsFileMerge.write(AlignmentsFileOneHotOffenZ[1])

def FindMax(Path):
	PathFolder = os.listdir(Path)
	maxlength = 0
	for Files in PathFolder:
		x = open(Path+'\\'+Files)
		xZ = x.readlines()
		if int(len(xZ[1]))>maxlength:
			print(maxlength)
			print(Files)
			maxlength = int(len(xZ[1]))
	return maxlength
def Punkt9_AlignmentsMergeAuffuelllen():
	AlignmentsOneHotMerge = os.listdir('D:\Masterarbeit\ZinkFinger\AlignmentsZF_onehot_stockholm_merge')
	CreateFolder('D:\Masterarbeit\ZinkFinger\AlignmentsZF_onehot_merge_aufgefuellt2')

	max = (FindMax('D:\Masterarbeit\ZinkFinger\AlignmentsZF_onehot_stockholm_merge'))

	for file in AlignmentsOneHotMerge:
		newfile = open('D:\Masterarbeit\ZinkFinger\AlignmentsZF_onehot_merge_aufgefuellt2\\'+file, 'w')
		oldfile = open('D:\Masterarbeit\ZinkFinger\AlignmentsZF_onehot_stockholm_merge\\'+file, 'r')
		oldfileZ = oldfile.readlines()

		newfile.write(oldfileZ[0])
		#for i in range(0, int(int(max - (int(len(oldfileZ[1]))))/2)):
			#newfile.write('0')
		newfile.write(oldfileZ[1])
		luecke = int(int(max - (int(len(oldfileZ[1])))))
		#if int(max - (int(len(oldfileZ[1]))))/2%2 == 0:
		#for i in range(0, int(int(max - (int(len(oldfileZ[1]))))/2)):
		#for i in range(luecke + int(len(oldfileZ[1])), max):
		for i in range(0,luecke):
			newfile.write('0')
		#else:
		#	for i in range(0, int(int(max - (int(len(oldfileZ[1]))))/2-1)):
			#	newfile.write('0')

		#newfileZ = newfile.readlines()
		#print(len(newfileZ[1]))
		print('max')
		print(max)
def TESTPunkt9():
	list = os.listdir('D:\Masterarbeit\ZinkFinger\AlignmentsZF_onehot_merge_aufgefuellt2')
	for file in list:
		fileopen = open('D:\Masterarbeit\ZinkFinger\AlignmentsZF_onehot_merge_aufgefuellt2\\'+file)
		fileopenZ = fileopen.readlines()
		print(len(fileopenZ[1]))
def normalisiere(x):
	#y = x.reshape((int(x.shape[0]/4),4))
	y=x
	#print('hi los')
	#print(y)
	#print(sum(y))
	ysum = sum(y)
	#print(ysum)
	for i in range(0, 4):
		y[i] = y[i] / ysum
	#print('pseudo')
	#print(y)
	#print(sum(y))
	return y
def aufgefuelltepwms():
	pwmlist = os.listdir('D:\Masterarbeit\ZinkFinger\PWMS')
	CreateFolder('D:\Masterarbeit\ZinkFinger\PWMSaufgefuellt')
	for file in pwmlist:
		pwmalt = open('D:\Masterarbeit\ZinkFinger\PWMS\\'+file)
		PwmFileXZ = pwmalt.readlines()
		output = open('D:\Masterarbeit\ZinkFinger\PWMSaufgefuellt\\'+file, 'w')
		output.write(PwmFileXZ[0])
		#Gerade Anzahl
		if len(PwmFileXZ)%2!=0:
			print('Gerade')
			for i in range(0, int((204-len(PwmFileXZ)*4)/2)):
				output.write(str(0.25))
				if (i%4==3) & (i>1):
					output.write('\n')
				else:
					output.write('\t')
			#Füge PWM In die Liste ein
			for i in range(1, len(PwmFileXZ)):
				pwmpseudo = []
				for j in range(0, len(PwmFileXZ[i].split('\t'))):
					pwmpseudo.append(float(PwmFileXZ[i].split('\t')[j].split('\n')[0])+0.05)
				pwmpseudo = normalisiere(pwmpseudo)
				for j in range(0, len(pwmpseudo)):
					output.write(str(pwmpseudo[j]))
					if j==3:
						output.write('\n')
					else:
						output.write('\t')

			for i in range(0, int((204-len(PwmFileXZ)*4)/2)):
				output.write(str(0.25))
				if (i%4==3) & (i>1):
					output.write('\n')
				else:
					output.write('\t')

		else:
			print('Ungerade')
			for i in range(0, int((204-len(PwmFileXZ)*4)/2)+2):
				output.write(str(0.25))
				if (i%4==3) & (i>1):
					output.write('\n')
				else:
					output.write('\t')
			#Füge PWM In die Liste ein
			for i in range(1, len(PwmFileXZ)):
				pwmpseudo = []
				for j in range(0, len(PwmFileXZ[i].split('\t'))):
					pwmpseudo.append(float(PwmFileXZ[i].split('\t')[j].split('\n')[0])+0.05)
				pwmpseudo = normalisiere(pwmpseudo)
				print(pwmpseudo)
				for j in range(0, len(pwmpseudo)):
					output.write(str(pwmpseudo[j]))
					if j==3:
						output.write('\n')
					else:
						output.write('\t')
			for i in range(0, int((204-len(PwmFileXZ)*4)/2)-2):
				output.write(str(0.25))
				if (i%4==3) & (i>1):
					output.write('\n')
				else:
					output.write('\t')
def Punkt10_MergeAlignmentsPwms():
	AlignmentsFolder = os.listdir('D:\Masterarbeit\ZinkFinger\AlignmentsZF_onehot_merge_aufgefuellt2\\')
	AlignmentsFolder.sort()
	output = open('D:\Masterarbeit\ZinkFinger\Input_NeuronalesNetzAlignment4.tsv', 'w')
	pwmlist = os.listdir('D:\Masterarbeit\ZinkFinger\PWMSaufgefuellt')

	#Gehe Alle Alignment-Files durch

	for AlignmentFile in AlignmentsFolder:
		if 'aln' in AlignmentFile:
			AlignmentFileX = open('D:\Masterarbeit\ZinkFinger\AlignmentsZF_onehot_merge_aufgefuellt2\\'+AlignmentFile)
			AlignmentFileXZ = AlignmentFileX.readlines()

			#Suche zugehoerige PWM Datei
			for pwms in pwmlist:
				if AlignmentFile.split('.')[0] in pwms:
					print(pwms)

					#In Zeile [0] -> Motiv-ID, In Zeile [1] -> Sequence
					for i in range(0, len(AlignmentFileXZ[1])):
						j = i + 1
						output.write(str(AlignmentFileXZ[1][i:j])+'\t')
					PwmFileX = open('D:\Masterarbeit\ZinkFinger\PWMSaufgefuellt\\'+AlignmentFile.split('.')[0]+'.'+AlignmentFile.split('.')[1]+'.pwm')
					PwmFileXZ = PwmFileX.readlines()

					for i in range(1, len(PwmFileXZ)):
						for j in range(0, len(PwmFileXZ[i].split('\t'))):
							output.write(str(float(PwmFileXZ[i].split('\t')[j].split('\n')[0])))
							output.write('\t')
					output.write('\n')

def TESTPunkt10():
	x = open('D:\Masterarbeit\ZinkFinger\Input_NeuronalesNetzAlignment2.tsv')
	xZ = x.readlines()
	print('zeilen.')
	print(len(xZ))
	for i in range(0,len(xZ)):
		print(len(xZ[i]))
def deletepwmsDBD():
	dbdslist = os.listdir('D:\Masterarbeit\ZinkFinger\DBDsALL')
	pwmlist = os.listdir('D:\Masterarbeit\ZinkFinger\PWMS')
	CreateFolder('D:\Masterarbeit\ZinkFinger\DBDsALL_new')
	for folder in dbdslist:
		folderlist = os.listdir('D:\Masterarbeit\ZinkFinger\DBDsALL\\'+folder)
		for files in folderlist:
			i = 0
			for pwm in pwmlist:
				if files in pwm:
					i = i + 1
					CreateFolder('D:\Masterarbeit\ZinkFinger\DBDsALL_new\\'+folder)
					oldpwm = open('D:\Masterarbeit\ZinkFinger\DBDsALL\\'+folder+'\\'+files)
					oldpwmZ = oldpwm.readlines()
					newpwm = open('D:\Masterarbeit\ZinkFinger\DBDsALL_new\\'+folder+'\\'+files, 'w')
					for zeile in range(0,len(oldpwmZ)):
						newpwm.write(oldpwmZ[zeile])
			if i == 0:
				print(files)
			print(i)
def Punkt11_Zufallsliste():
	alignmentsliste = os.listdir('D:\Masterarbeit\ZinkFinger\AlignmentsZF_onehot_merge_aufgefuellt')
	pwmlist = os.listdir('D:\Masterarbeit\ZinkFinger\PWMS')
	DBDList = os.listdir('D:\Masterarbeit\ZinkFinger\DBDsALL_new')
	CreateFolder('D:\Masterarbeit\ZinkFinger\zufallsliste')
	dict_tffaktors = {}
	#1. Erzeuge Dict keys = TF, values = list von motiv-ids
	for tffaktor in DBDList:
		tffaktorlist = os.listdir('D:\Masterarbeit\ZinkFinger\DBDsALL_new\\'+tffaktor)
		dict_tffaktors[tffaktor] = list()
		for motivid in tffaktorlist:
			dict_tffaktors[tffaktor].append(motivid)
	#print(dict_tffaktors)
	rng = default_rng()
	liste = list(dict_tffaktors.keys())
	#Erzeuge Zufallsliste
	for anzahlliste in range(1,10):
		doppeltzufalllistevermeiden = []
		zufallsliste = []
		i=0
		while i <=(int(len(alignmentsliste))*0.75):
			zufallszahl = int(rng.choice(range(0,len(dict_tffaktors)), size = 1))
			#Test ob zufallszahl bereits in liste
			if zufallszahl not in doppeltzufalllistevermeiden:
				doppeltzufalllistevermeiden.append(zufallszahl)
				for k in range(0,len(dict_tffaktors[liste[zufallszahl]])):
					for motivid in range(0,len(pwmlist)):
						if dict_tffaktors[liste[zufallszahl]][k] == pwmlist[motivid]:
							zufallsliste.append(int(motivid))
				i = i + len(dict_tffaktors[liste[zufallszahl]])
		zufallsliste.sort()
		np.save('D:\Masterarbeit\ZinkFinger\zufallsliste\zufallsliste_neu'+str(anzahlliste)+'.npy',zufallsliste)
def Punkt12_Homeodomain():
	pwmslist = os.listdir('D:\Masterarbeit\Daten\PWM_shifts_full')
	output = open('D:\Masterarbeit\ZinkFinger\Input_NeuronalesNetzAlignmentHomeodomainTEST.tsv', 'w')
	alignmentspfad = 'D:\Masterarbeit\Daten\Alignments_onehot_ueberarbeitet'
	for pwm in pwmslist:
		pwmopen = open('D:\Masterarbeit\Daten\PWM_shifts_full\\'+pwm)
		pwmopenZ = pwmopen.readlines()
		alignmentopen = open(alignmentspfad+'\\'+pwm.split('.')[0]+'.'+pwm.split('.')[1]+'.aln')
		alignmentopenZ = alignmentopen.readlines()

		for i in range(0, len(alignmentopenZ)):
			#j = i + 1
			output.write(str(int(float(alignmentopenZ[i].split('\n')[0])))+'\t')

		for i in range(1, len(pwmopenZ)):
			if pwmopenZ[i].split('\t')[0] == '0,25':
				output.write(str(0)+'\t'+str(0)+'\t'+str(0)+'\t'+str(0)+'\t')
				#if i < len(pwmopenZ)-1:
				#	output.write('\t')
				#else:
					#output.write('\n')
			else:
				for j in range(0, len(pwmopenZ[i].split('\t'))):
					output.write(str(pwmopenZ[i].split('\t')[j].split('\n')[0])+'\t')
		output.write('\n')
def TESTINhalt():
	x = os.listdir('D:\Masterarbeit\ZinkFinger\AlignmentsZF_onehot_merge_aufgefuellt')
	x2 = os.listdir('D:\Masterarbeit\ZinkFinger\AlignmentsZFVorherOhneGAPS')
	for file in x2:
		test = open('D:\Masterarbeit\ZinkFinger\AlignmentsZF_onehot_merge_aufgefuellt\\'+file.split('.')[0]+'.00.aln')








Punkt6_SplitMultiplesAlignment()
Punkt7_AlignmentsOnehot()
Punkt8_FuegeEinzelneAlignmentFilesJEWEILSZusammen()
Punkt9_AlignmentsMergeAuffuelllen()
TESTPunkt9()
aufgefuelltepwms()
Punkt10_MergeAlignmentsPwms()
TESTPunkt10()
deletepwmsDBD()
Punkt11_Zufallsliste()
Punkt12_Homeodomain()
TESTINhalt()
