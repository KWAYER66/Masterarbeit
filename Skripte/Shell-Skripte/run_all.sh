
#!/bin/bash


eval "$(conda shell.bash hook)"
conda activate tensorflow

cd ..
cd NeuronalesNetz

for neuronalesnetz in * ; do
	for ((i=1;i<=5;i++)) ; do
		for ((j=1;j<=5;j++)) ; do
			for k in {0..100..10} ; do
				for e in {500..2000..500} ; do
					bash D:/Masterarbeit/Skripte/Shell-Skripte/Run_NeuronalesNetz.sh 176 $i $k $j $e $neuronalesnetz
					bash D:/Masterarbeit/Skripte/Shell-Skripte/Run_NeuronalesNetz.sh 140 $i $k $j $e $neuronalesnetz

				done	
			done
		done
	done
done


cd ..
cd Shell-Skripte
bash Datennachbereitung_Auswertung.sh
