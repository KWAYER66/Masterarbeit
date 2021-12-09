
#!/bin/bash


eval "$(conda shell.bash hook)"
conda activate tensorflow

cd ..
cd ..
cd Predictions

for predict in * ; do
	for ((i=1;i<=2;i++)) ; do
		for j in {120..320..100} ; do
			for k in {1..2..1} ; do
				Python MLPClassifier.py 176 $i $j $k
			done
		done
	done
done
