
#!/bin/bash

#Variablen Deklarieren
#[ -n "$1" ] && a=$1 || { echo -n "Enter Pfad zu NeuronalesNetz oder 0: "; read a; }
#[ -n "$2" ] && b=$2 || { echo -n "Enter 176 oder 140: "; read b; }
#[ -n "$3" ] && c=$3 || { echo -n "Enter Iterationen: "; read c; }
#[ -n "$4" ] && d=$4 || { echo -n "Enter WeightFaktor: "; read d; }
#[ -n "$5" ] && e=$5 || { echo -n "Enter Epochen: " read e; }



eval "$(conda shell.bash hook)"
conda activate tensorflow

#Python Skript zur Datennachbereitung und Auswertung
Python D:/Masterarbeit/Skripte/Datennachbearbeitung/Datennachbearbeitung.py

"C:/Program Files/R/R-3.6.1/bin/Rscript" D:/Masterarbeit/Skripte/Datennachbearbeitung/Plots_KL_DIVTEST.R

#Plotten der SeqLogo und DiffLogo
"C:/Program Files/R/R-3.6.1/bin/Rscript" D:/Masterarbeit/Skripte/Datennachbearbeitung/Difflogo_R.R
