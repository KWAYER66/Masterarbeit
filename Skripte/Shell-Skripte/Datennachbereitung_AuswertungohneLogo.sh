
#!/bin/bash

eval "$(conda shell.bash hook)"
conda activate tensorflow

#Python Skript zur Datennachbereitung und Auswertung
Python D:/Masterarbeit/Skripte/Datennachbearbeitung/Datennachbearbeitung_run_all.py

#Plots fuer KL_Divergence der TestDaten
"C:/Program Files/R/R-3.6.1/bin/Rscript" D:/Masterarbeit/Skripte/Datennachbearbeitung/Plots_KL_DIVTEST.R

#Auswertung Zuordnungen
Python D:/Masterarbeit/Skripte/Datennachbearbeitung/auswertungZuordnung_Sicherheitsmas51.py

#Boxplots fuer Representanten 
"C:/Program Files/R/R-3.6.1/bin/Rscript" D:/Masterarbeit/Skripte/Datennachbearbeitung/boxplotrepresentant.R

#Zuordnung Hist
"C:/Program Files/R/R-3.6.1/bin/Rscript" D:/Masterarbeit/Skripte/Datennachbearbeitung/Plot_Gruppenzuordnung.R
