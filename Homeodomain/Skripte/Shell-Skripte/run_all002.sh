
#!/bin/bash


eval "$(conda shell.bash hook)"
conda activate tensorflow

cd ..
cd NeuronalesNetz_richtig

for ((i=2;i<=5;i++)) ; do 
	bash D:/Masterarbeit/Skripte/Shell-Skripte/Run_NeuronalesNetz.sh 176 $i 1 4 500 NeuronalesNetz_002.py			
done
