
#!/bin/bash

#Variablen Deklarieren
[ -n "$1" ] && a=$1 || { echo -n "Enter Pfad zu NeuronalesNetz oder 0: "; read a; }
[ -n "$2" ] && b=$2 || { echo -n "Enter 176 oder 140: "; read b; }
[ -n "$3" ] && c=$3 || { echo -n "Enter Iterationen: "; read c; }
[ -n "$4" ] && d=$4 || { echo -n "Enter WeightFaktor: "; read d; }
[ -n "$5" ] && e=$5 || { echo -n "Enter Epochen: " read e; }



eval "$(conda shell.bash hook)"
conda activate tensorflow


#Setze Punkte anstatt Kommas bei den InputPWMs ... 	BEREITSS ERLEDIGT!!!!
#Python D:/Inferenz_von_TF_Bindepraeferenzen/Pipeline/kommasinpunkte.py
#Python D:/Inferenz_von_TF_Bindepraeferenzen/Pipeline/kommasinpunkteG.py

#Pfad zum speichern der Ergebnisse
predictionspfad="D:\Inferenz_von_TF_Bindepraeferenzen\Predictions_NeuronalesNetz"

bash pipeline_Neuronales_Netz.sh $a $b $c $d $e

	#Uebersetze die Predictions.npy Datei in das PWM Format
Python D:/Inferenz_von_TF_Bindepraeferenzen/Pipeline/UbersetzungPredictionsMultipleOutputs.py $predictionspfad

	#Berechne die KL-Divergence fuer jeden TF
Python D:/Inferenz_von_TF_Bindepraeferenzen/Pipeline/kl_divergenceMultipleOutputs.py $predictionspfad

#	Berechne durchschnittliche KL-Divergence pro Gruppe
Python D:/Inferenz_von_TF_Bindepraeferenzen/Pipeline/durchschnittkl_divMultipleOutputs.py $predictionspfad

#Berechne die KL-Divergence fuer jeden TF pro Gruppe
Python D:/Inferenz_von_TF_Bindepraeferenzen/Pipeline/SchaetzungJeGruppeMultipleOutputs.py $predictionspfad


Python D:/Inferenz_von_TF_Bindepraeferenzen/Pipeline/zufallslistsundtests.py $predictionspfad
"C:/Program Files/R/R-3.6.1/bin/Rscript" D:/Inferenz_von_TF_Bindepraeferenzen/Pipeline/Plots_KL_DIVTEST
#Plotten der SeqLogo und DiffLogo

#for ((i=1;i<=$c;i++))
#do
#"C:/Program Files/R/R-3.6.1/bin/Rscript" D:/Inferenz_von_TF_Bindepraeferenzen/Pipeline/Difflogo_R.R $b $i $d $e
#done
