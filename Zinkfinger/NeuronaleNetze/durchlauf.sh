
#!/bin/bash


eval "$(conda shell.bash hook)"
conda activate tensorflow

for ((i=2;i<=5;i++)) ; do
	echo 'hi'
	Python NeuronalesNetz_001.py 200 $i
	Python NeuronalesNetz_002.py 200 $i
	Python NeuronalesNetz_003.py 200 $i
	Python NeuronalesNetz_004.py 200 $i
	Python NeuronalesNetz_005.py 200 $i
	Python NeuronalesNetz_006.py 200 $i
	Python NeuronalesNetz_007.py 200 $i
	Python NeuronalesNetz_008.py 200 $i
	Python NeuronalesNetz_011.py 200 $i
	Python NeuronalesNetz_012.py 200 $i
	Python NeuronalesNetz_026.py 200 $i
	Python NeuronalesNetz_027.py 200 $i
	Python NeuronalesNetz_013.py 200 $i
	Python NeuronalesNetz_014.py 200 $i
	Python NeuronalesNetz_015.py 200 $i
	Python NeuronalesNetz_016.py 200 $i
	Python NeuronalesNetz_017.py 200 $i
	Python NeuronalesNetz_018.py 200 $i
	Python NeuronalesNetz_202.py 200 $i
	Python NeuronalesNetz_203.py 200 $i
	Python NeuronalesNetz_302.py 200 $i
	Python NeuronalesNetz_303.py 200 $i
	Python NeuronalesNetz_402.py 200 $i
	Python NeuronalesNetz_403.py 200 $i
	Python NeuronalesNetz_502.py 200 $i
	Python NeuronalesNetz_503.py 200 $i
	Python NeuronalesNetz_602.py 200 $i
	Python NeuronalesNetz_603.py 200 $i

done

cd ..
Python ZF_Datennachbearbeitung_new.py
#"C:/Program Files/R/R-3.6.1/bin/Rscript" D:/Masterarbeit/ZinkFinger/Difflogo_Reinzeln,R
