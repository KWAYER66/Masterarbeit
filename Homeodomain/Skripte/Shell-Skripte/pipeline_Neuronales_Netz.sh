#!/bin/bash


#Deklariere Variablen (Einstellungen fuer das Neuronale Netz)
#$1 = Pfad zu neuronalen Netz
[ -n "$1" ] && PfadNeuronalesNetz=$1 || { echo -n "Enter Pfad NeuronalesNetz: "; read PfadNeuronalesNetz; }

if [[ $1 == 0 ]]; then	
	PfadNeuronalesNetz="D:/Inferenz_von_TF_Bindepraeferenzen/Pipeline/NeuronalesNetzAktuell/InferenzTFBindepraeferenzen_NeuronalesNetz.py"
fi

#$2 = 176 fuer ALLE 140 fuer Gruppe
[ -n "$2" ] && AlleGruppen=$2 || { echo -n "Enter Alle (176) oder Gruppen (140): "; read AlleGruppen; }
#Input Datei ist abhaengig von AlleGruppe var
if [[ $AlleGruppen == 176 ]]; then
	PfadInput="D:/Inferenz_von_TF_Bindepraeferenzen/AlignmentPWMBeide/AlignmentsPWMs.npy"
else
	PfadInput="D:/Inferenz_von_TF_Bindepraeferenzen/AlignmentPWMBeide/AlignmentsPWMsNachGruppen.npy"
fi
#$3 = Iterationen (Wie oft soll das Netz ausgefuert werden)
[ -n "$3" ] && Iterationen=$3 || { echo -n "Enter Iterationen des NeuronalenNetzes: "; read Iterationen; }
#$4 = Faktor Weights
[ -n "$4" ] && Weights=$4 || { echo -n "Enter WeightsFaktor: "; read Weights; }
#$5 = Epochen 
[ -n "$5" ] && Epochen=$5 || { echo -n "Enter EpochenAnzahl: "; read Epochen; }


eval "$(conda shell.bash hook)"
conda activate tensorflow

for ((i=1;i<=$Iterationen;i++))
do
Python $PfadNeuronalesNetz $PfadInput $AlleGruppen $i $Weights $Epochen
done
