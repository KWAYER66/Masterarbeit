
#!/bin/bash


eval "$(conda shell.bash hook)"
conda activate tensorflow

cd ..
cd NeuronalesNetz

for neuronalesnetz in * ; do
	for ((i=1;i<=1;i++)) ; do
		for ((j=4;j<=4;j++)) ; do
			for k in {1..1..999} ; do
				for e in {500..500..500} ; do
					bash D:/Masterarbeit/Skripte/Shell-Skripte/Run_NeuronalesNetz.sh 176 $i $k $j $e $neuronalesnetz					
				done	
			done
		done
	done
done


cd ..
cd Shell-Skripte
bash Datennachbereitung_AuswertungohneLogo.sh
#"C:/Program Files/R/R-3.6.1/bin/Rscript" D:/Masterarbeit/Skripte/Datennachbearbeitung/Difflogo_R.R
"C:/Program Files/R/R-3.6.1/bin/Rscript" D:/Masterarbeit/Skripte/Datennachbearbeitung/Scatterplot_Sicherheitsmas_KL_div.R
