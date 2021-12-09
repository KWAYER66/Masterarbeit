
#!/bin/bash

eval "$(conda shell.bash hook)"
conda activate tensorflow

#Python Skript zur Datennachbereitung und Auswertung
Python D:/Masterarbeit/Skripte/Datennachbearbeitung/Datennachbearbeitung.py

#Plots fuer KL_Divergence der TestDaten
#"C:/Program Files/R/R-3.6.1/bin/Rscript" D:/Masterarbeit/Skripte/Datennachbearbeitung/Plots_KL_DIVTEST.R

#Plotten der SeqLogo und DiffLogo
"C:/Program Files/R/R-3.6.1/bin/Rscript" D:/Masterarbeit/Skripte/Datennachbearbeitung/Difflogo_R.R
