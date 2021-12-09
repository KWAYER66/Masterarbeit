import os, sys
import numpy as np
from numpy import genfromtxt
from numpy import savetxt
import tensorflow as tf
from tensorflow.python.ops import nn
from tensorflow.python.keras import backend
import tensorflow.keras.backend as K
from tensorflow.python.framework import ops
from tensorflow.python.ops import math_ops
from random import sample
from random import random
from numpy.random import default_rng

def softmax_by_christian(x, axis=-1):
  x = tf.reshape(x,shape=[-1,int(x.shape[1]/4),4])

  if x.shape.rank > 1:
    if isinstance(axis, int):
        output = nn.softmax(x, axis=axis)
    else:
      # nn.softmax does not support tuple axis.
      e = math_ops.exp(x - math_ops.reduce_max(x, axis=axis, keepdims=True))
      s = math_ops.reduce_sum(e, axis=axis, keepdims=True)
      output = e / s
  else:
    raise ValueError('Cannot apply softmax to a tensor that is 1D. '
                     'Received input: %s' % (x,))
  output = tf.reshape(output,shape=[-1,output.shape[1]*4])
  output._keras_logits = x
  return output
def kl_divergence_by_christian(y_true, y_pred):
	#print(y_true)
	#Add Pseudocounts
	y_true2 = tf.math.add(y_true, 0.01)
	#print(y_true)
	y_true2 = softmax_by_christian(y_true2)

	print(tf.math.subtract(y_true, y_true2))



	y_pred = ops.convert_to_tensor_v2_with_dispatch(y_pred)
	y_true = math_ops.cast(y_true, y_pred.dtype)
	y_true = backend.clip(y_true, backend.epsilon(), 1)
	y_pred = backend.clip(y_pred, backend.epsilon(), 1)
	return math_ops.reduce_sum(y_true * math_ops.log(y_true / y_pred), axis=-1)
def Berechne_KL_Divergence_Ohne_PWMs_erzeugen():
	pfadpredpwms = os.listdir('D:\Masterarbeit\Predictions')
	for datei in pfadpredpwms:
		if ('prediction' in datei) & ('176' in datei):
			tsvdateimitdivergencen = open('D:\Masterarbeit\Predictions'+'\\'+datei+'\kl_divergencen.tsv','w')
			pwm = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights.npy')
			pwm = pwm[:,6804:(6804+176)]
			pred = np.load('D:\Masterarbeit\Predictions\\'+datei+'\\'+datei+'.npy')
			for i in range(0,5):
				altpwm = np.asarray(pwm[i,])[np.newaxis]
				prepwm = np.asarray(pred[i,])[np.newaxis]
				x = kl_divergence_by_christian(altpwm,prepwm)
				tsvdateimitdivergencen.write(str(np.asarray(x[0,]))+'\n')
		elif ('prediction' in datei) & ('140' in datei):
			tsvdateimitdivergencen = open('D:\Masterarbeit\Predictions'+'\\'+datei+'\kl_divergencen.tsv','w')
			pwm = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMsGruppen_Zuordnung_Weights.npy')
			pwm = pwm[:,6804:(6804+140)]
			pred = np.load('D:\Masterarbeit\Predictions\\'+datei+'\\'+datei+'.npy')
			for i in range(0,pwm.shape[0]):
				altpwm = np.asarray(pwm[i,])[np.newaxis]
				prepwm = np.asarray(pred[i,])[np.newaxis]
				x = kl_divergence_by_christian(altpwm,prepwm)
				tsvdateimitdivergencen.write(str(np.asarray(x[0,]))+'\n')

Berechne_KL_Divergence_Ohne_PWMs_erzeugen()
