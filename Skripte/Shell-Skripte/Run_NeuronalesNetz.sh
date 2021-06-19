#!/bin/bash


#Deklariere Variablen (Einstellungen fuer das Neuronale Netz)

#$1 = 176 fuer ALLE 140 fuer Gruppe
[ -n "$1" ] && AlleGruppen=$1 || { echo -n "Enter Alle (176) oder Gruppen (140): "; read AlleGruppen; }
#$2 = Iterationen (Wie oft soll das Netz ausgefuert werden)
[ -n "$2" ] && Iterationen=$2 || { echo -n "Enter Iterationen des NeuronalenNetzes: "; read Iterationen; }
#$3 = Faktor Weights
[ -n "$3" ] && Weights=$3 || { echo -n "Enter WeightsFaktor: "; read Weights; }
#$4 = Train Test Split List
[ -n "$4" ] && List=$4 || { echo -n "Enter Zufallslist: "; read List; }
#$5 = Epochen 
[ -n "$5" ] && Epochen=$5 || { echo -n "Enter EpochenAnzahl: "; read Epochen; }
#$6 = PfadNeuronalesNetz
[ -n "$6" ] && PfadNeuronalesNetz=$6 || { echo -n "Enter PfadNeuronalesNetz: "; read PfadNeuronalesNetz; }

eval "$(conda shell.bash hook)"
conda activate tensorflow


Python $PfadNeuronalesNetz $AlleGruppen $Iterationen $Weights $List $Epochen
