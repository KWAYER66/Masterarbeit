
#!/bin/bash



cd ..
cd ..
cd DBDs

for tffaktor in * ; do
	cd $tffaktor
	dir=$(pwd)
	outputpfad="${dir}ergebnis"
	mkdir $outputpfad
	java -jar D:/Masterarbeit/Skripte/Java/PWMShifts-0.2.jar p="$dir" k=8 c=0.5 outdir="$outputpfad"
	cd ..
done
