import sys, os
import gzip
import shutil
import numpy as np


folderIdMaps = os.listdir('D:\Masterarbeit\ZinkFinger\ID_Maps')
folderAlignments = os.listdir('D:\Masterarbeit\ZinkFinger\Alignments')
CisBp = os.listdir('D:\Masterarbeit\ZinkFinger\CisBP_2021_08_06_7_21_am')

def CreateFolder(Path):
	if os.path.exists(Path) == False:
		os.makedirs(Path)
#Funktion - Finde ALLE zf-C2H2.map.tab Dateien
def Punkt1_FindezfC2H2(folderIdMaps):
    ListKorrekteIdMaps = []
    Motiv = 'zf-C2H2'
    for IdMap in folderIdMaps:
        detektor = 1
        NameIdMap = IdMap.split('.')[0].split(',')
        for Position in NameIdMap:
            if Position != Motiv:
                detektor = 0
        if detektor == 1:
            ListKorrekteIdMaps.append(IdMap)
    return ListKorrekteIdMaps
#Function - Erstelle Je MotivID eine PWM
def Punkt1_ErstellePWM(MotivID, IdMap, TfID):
	pwm1 = open('D:\Masterarbeit\ZinkFinger\DBDsALL\\'+TfID+'\\'+MotivID+'.pwm', 'w')
	pwm2 = open('D:\Masterarbeit\ZinkFinger\DBDsNachFile\\'+IdMap+'\\'+TfID+'\\'+MotivID+'.pwm', 'w')
	pwm3 = open('D:\Masterarbeit\ZinkFinger\PWMS\\'+MotivID+'.pwm', 'w')

	PWMtxt = open('D:\Masterarbeit\ZinkFinger\CisBP_2021_08_06_7_21_am\PWM.txt')
	PWMtxtZ = PWMtxt.readlines()

	for Zeile in range(0, len(PWMtxtZ)):
		if MotivID in PWMtxtZ[Zeile]:
			pwm1.write('>'+MotivID+'\n')
			pwm2.write('>'+MotivID+'\n')
			pwm3.write('>'+MotivID+'\n')

			i = 0
			while len(PWMtxtZ[Zeile+4+i]) != 1:
				for j in range(1,4):
					pwm1.write(str(PWMtxtZ[Zeile+4+i].split('\t')[j])+'\t')
					pwm2.write(str(PWMtxtZ[Zeile+4+i].split('\t')[j])+'\t')
					pwm3.write(str(PWMtxtZ[Zeile+4+i].split('\t')[j])+'\t')
				pwm1.write(str(PWMtxtZ[Zeile+4+i].split('\t')[4]))
				pwm2.write(str(PWMtxtZ[Zeile+4+i].split('\t')[4]))
				pwm3.write(str(PWMtxtZ[Zeile+4+i].split('\t')[4]))
				i = i + 1
#Function - Finde Ueberlappungen zwischen ID-Map und TF-Information
def Punkt1_FindeUeberlappungIdMapTFInfoPWMS(IdMap):
	TF_Information = open('D:\Masterarbeit\ZinkFinger\CisBP_2021_08_06_7_21_am\TF_Information.txt')
	TF_InformationZ = TF_Information.readlines()
	IdMapData = open('D:\Masterarbeit\ZinkFinger\ID_Maps\\'+IdMap)
	IdMapDataZ = IdMapData.readlines()
	CreateFolder('D:\Masterarbeit\ZinkFinger\DBDsALL')
	CreateFolder('D:\Masterarbeit\ZinkFinger\DBDsNachFile\\'+str(IdMap))
	CreateFolder('D:\Masterarbeit\ZinkFinger\PWMS')

	for i in range(0, len(IdMapDataZ)):
		for j in range(0, len(TF_InformationZ)):
			if IdMapDataZ[i].split('\t')[3].split('\n')[0] in TF_InformationZ[j]:
				CreateFolder('D:\Masterarbeit\ZinkFinger\DBDsALL\\'+str(TF_InformationZ[j].split('\t')[0]))
				CreateFolder('D:\Masterarbeit\ZinkFinger\DBDsNachFile\\'+str(IdMap)+'\\'+str(TF_InformationZ[j].split('\t')[0]))
				MotivIDsProDBD = []
				for CounterMotivID in range(6, len(TF_InformationZ[j].split('\t'))):
					MotivIDsProDBD.append(str(TF_InformationZ[j].split('\t')[CounterMotivID].split(',')[0]))
				for k in range(0, len(MotivIDsProDBD)):
					ErstellePWM(MotivIDsProDBD[k], str(IdMap), str(TF_InformationZ[j].split('\t')[0]))
#Funktion - Erstelle Alignments
def Punkt1_ExtractAlignments():
	FolderNamen = os.listdir('D:\Masterarbeit\ZinkFinger\DBDsNachFile')
	AlignmentsPfad = 'D:\Masterarbeit\ZinkFinger\Alignments'
	for File in FolderNamen:
		with gzip.open(AlignmentsPfad+'\\'+File.split('.')[0]+'.aln.gz', 'rb') as f_in:
			with open(AlignmentsPfad+'\\'+File.split('.')[0]+'.aln', 'wb') as f_out:
				shutil.copyfileobj(f_in, f_out)
def Punkt1_FindeUeberlappungIdMapTFInfoAlignments(IdMap):
	TF_Information = open('D:\Masterarbeit\ZinkFinger\CisBP_2021_08_06_7_21_am\TF_Information.txt')
	TF_InformationZ = TF_Information.readlines()
	IdMapData = open('D:\Masterarbeit\ZinkFinger\ID_Maps\\'+IdMap)
	IdMapDataZ = IdMapData.readlines()
	CreateFolder('D:\Masterarbeit\ZinkFinger\AlignmentsZF')
	CreateFolder('D:\Masterarbeit\ZinkFinger\AlignmentsZFNachFile')
	CreateFolder('D:\Masterarbeit\ZinkFinger\AlignmentsZFDBDsAll')
	AlignmentData = open('D:\Masterarbeit\ZinkFinger\Alignments\\'+IdMap.split('.')[0]+'.aln')
	AlignmentDataZ = AlignmentData.readlines()



	for i in range(0, len(IdMapDataZ)):
		for j in range(0, len(TF_InformationZ)):
			if IdMapDataZ[i].split('\t')[3].split('\n')[0] in TF_InformationZ[j]:
				CreateFolder('D:\Masterarbeit\ZinkFinger\AlignmentsZFDBDsAll\\'+str(TF_InformationZ[j].split('\t')[0]))
				CreateFolder('D:\Masterarbeit\ZinkFinger\AlignmentsZFNachFile\\'+str(IdMap)+'\\'+str(TF_InformationZ[j].split('\t')[0]))
				MotivIDsProDBD = []
				for CounterMotivID in range(6, len(TF_InformationZ[j].split('\t'))):
					MotivIDsProDBD.append(str(TF_InformationZ[j].split('\t')[CounterMotivID].split(',')[0]))
				for k in range(0, len(MotivIDsProDBD)):
					Alignment = open('D:\Masterarbeit\ZinkFinger\AlignmentsZF\\'+MotivIDsProDBD[k]+'.aln', 'w')
					Alignment2 = open('D:\Masterarbeit\ZinkFinger\AlignmentsZFDBDsAll\\'+str(TF_InformationZ[j].split('\t')[0])+'\\'+MotivIDsProDBD[k]+'.aln', 'w')
					Alignment3 = open('D:\Masterarbeit\ZinkFinger\AlignmentsZFNachFile\\'+str(IdMap)+'\\'+str(TF_InformationZ[j].split('\t')[0])+'\\'+MotivIDsProDBD[k]+'.aln', 'w')


					Alignment.write('>'+MotivIDsProDBD[k]+'\n')
					Alignment2.write('>'+MotivIDsProDBD[k]+'\n')
					Alignment3.write('>'+MotivIDsProDBD[k]+'\n')
					Alignment.write(AlignmentDataZ[i].split('\t')[1])
					Alignment2.write(AlignmentDataZ[i].split('\t')[1])
					Alignment3.write(AlignmentDataZ[i].split('\t')[1])
def Punkt2_AlignmentsInEinzelnesFilesFasta():
	FolderAlignments = os.listdir('D:\Masterarbeit\ZinkFinger\AlignmentsZF')
	CreateFolder('D:\Masterarbeit\ZinkFinger\AlignmentsZFVorherOhneGAPS')
	for file in FolderAlignments:
		AlignmentFile = open('D:\Masterarbeit\ZinkFinger\AlignmentsZF\\'+file)
		AlignmentsFileOhneGAPS = open('D:\Masterarbeit\ZinkFinger\AlignmentsZFVorherOhneGAPS\\'+file.split('.')[0]+'.'+file.split('.')[1]+'.fasta', 'w')

		AlignmentFileZ = AlignmentFile.readlines()
		AlignmentsFileOhneGAPS.write(AlignmentFileZ[0])
		AlignmentString = AlignmentFileZ[1]

		AlignmentString = AlignmentString.replace("-", "")
		AlignmentsFileOhneGAPS.write(AlignmentString+'\n')
def Punkt10_MergeAlignmentsPwms():
	AlignmentsFolder = os.listdir('D:\Masterarbeit\ZinkFinger\AlignmentsZF_onehot\AlignmentsZF_onehot\\')
	final_array = []
	final_array = np.asarray(final_array)[np.newaxis]
	#Gehe Alle Alignment-Files durch
	for AlignmentFile in AlignmentsFolder:
		if 'aln' in AlignmentFile:
			AlignmentFileX = open('D:\Masterarbeit\ZinkFinger\AlignmentsZF_onehot\AlignmentsZF_onehot\\'+AlignmentFile)
			AlignmentFileXZ = AlignmentFileX.readlines()

			#array zum speichern einer Zeile
			arr = []

			#In Zeile [0] -> Motiv-ID, In Zeile [2] -> Sequence
			for i in range(0, len(AlignmentFileXZ[2])-1):
				j = i + 1
				arr.append(AlignmentFileXZ[2][i:j])

			#Suche zugehoerige PWM Datei
			print(AlignmentFile.split('_')[0]+'_'+AlignmentFile.split('_')[1]+'.pwm')
			PwmFileX = open('D:\Masterarbeit\ZinkFinger\PWMS\\'+AlignmentFile.split('_')[0]+'_'+AlignmentFile.split('_')[1]+'.pwm')
			PwmFileXZ = PwmFileX.readlines()

			#Füge PWM In die Liste ein
			for i in range(1, len(PwmFileXZ)):
				for j in range(0, len(PwmFileXZ[i].split('\t'))):
					arr.append(PwmFileXZ[i].split('\t')[j].split('\n')[0])

			#Final Array appenden
			myarray = np.asarray(arr)[np.newaxis]
			final_array = np.append(final_array, myarray, axis =1)
	np.save('D:\Masterarbeit\ZinkFinger\Input_NeuronalesNetz.npy', final_array)



print('Jetzt kommen die PWMS')
NamesIdMaps = FindezfC2H2(folderIdMaps)
for i in range(0, len(NamesIdMaps)):
	FindeUeberlappungIdMapTFInfoPWMS(NamesIdMaps[i])
print('Jetzt kommen die Alignments')
ExtractAlignments()
for i in range(0, len(NamesIdMaps)):
	FindeUeberlappungIdMapTFInfoAlignments(NamesIdMaps[i])

AlignmentsAllIn()

AllignmentsAllInEinzelnesFile()
AlignmentsInEinzelnesFilesFasta()


MergeAlignmentsPwms()
