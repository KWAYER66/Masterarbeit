#!/bin/bash

#bash pipeline_NeuronalesNachbereitung.sh 0 176 1 1 500
#bash pipeline_NeuronalesNachbereitung.sh 0 176 1 1 1000
#bash pipeline_NeuronalesNachbereitung.sh 0 176 1 5 1000
#bash pipeline_NeuronalesNachbereitung.sh 0 176 1 10 1000
#bash pipeline_NeuronalesNachbereitung.sh 0 176 1 20 500
#bash pipeline_NeuronalesNachbereitung.sh 0 140 1 1 500
#bash pipeline_NeuronalesNachbereitung.sh 0 140 1 5 500
#bash pipeline_NeuronalesNachbereitung.sh 0 140 1 20 500
bash pipeline_NeuronalesNachbereitung.sh D:/Inferenz_von_TF_Bindepraeferenzen/NeuronalesNetz_T1.py 176 1 1 500
bash pipeline_NeuronalesNachbereitung.sh D:/Inferenz_von_TF_Bindepraeferenzen/NeuronalesNetz_T2.py 176 1 1 501
bash pipeline_NeuronalesNachbereitung.sh D:/Inferenz_von_TF_Bindepraeferenzen/NeuronalesNetz_T3.py 176 1 1 502
bash pipeline_NeuronalesNachbereitung.sh D:/Inferenz_von_TF_Bindepraeferenzen/NeuronalesNetz_T4.py 176 1 1 503

