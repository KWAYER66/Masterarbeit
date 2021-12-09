import numpy as np
import tensorflow as tf
from numpy import genfromtxt
from numpy import savetxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout, Conv1D, Flatten, GlobalMaxPooling1D, GlobalAveragePooling1D,Reshape, LSTM
import sys
import os
from sklearn.metrics import roc_auc_score,accuracy_score
from sklearn.model_selection import StratifiedKFold
from tensorflow.keras.models import clone_model
from tensorflow.python.ops import nn
from tensorflow.python.keras import backend
import tensorflow.keras.backend as K
from tensorflow.python.framework import ops
from tensorflow.python.ops import math_ops
from random import sample
from random import random
from numpy.random import default_rng
import io
from contextlib import redirect_stdout

if os.path.exists('D:\Masterarbeit\Predictions\prediction'+sys.argv[0].split('_')[1].split('.')[0]+'_'+sys.argv[1]+'_'+sys.argv[2]+'_'+sys.argv[3]+'_'+sys.argv[4]+'_'+sys.argv[5]) == False:
	os.makedirs('D:\Masterarbeit\Predictions\prediction'+sys.argv[0].split('_')[1].split('.')[0]+'_'+sys.argv[1]+'_'+sys.argv[2]+'_'+sys.argv[3]+'_'+sys.argv[4]+'_'+sys.argv[5])
#sys.argv[1] -> Bestimmt die Inputdatei und die Anzahl der Neuronen im Output Layer
if sys.argv[1] == '176':
	datapfad = 'D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights_Abst_tf.npy'
elif sys.argv[1] == '140':
	datapfad = 'D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMsGruppen_Zuordnung_Weights.npy'
#sys.argv[2] -> Index der Iterationen zum Speichern der Datei
#sys.argv[3] -> Faktor fuer sample_weights
#sys.argv[4] -> Bestimme Train/Test - Split
#sys.argv[5] -> Anzahl an Epochen

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
  y_pred = ops.convert_to_tensor_v2_with_dispatch(y_pred)
  y_true = math_ops.cast(y_true, y_pred.dtype)
  y_true = backend.clip(y_true, backend.epsilon(), 1)
  y_pred = backend.clip(y_pred, backend.epsilon(), 1)
  return math_ops.reduce_sum(y_true * math_ops.log(y_true / y_pred), axis=-1)
def js_divergence(p, q):
	m = 0.5 * (p + q)
	return 0.5 * kl_divergence_by_christian(p, m) + 0.5 * kl_divergence_by_christian(q, m)
def train_model(X,Y,weights):
    model1 = Sequential()
    model1.add(Dense(int(sys.argv[1]),activation="relu"))
    model1.add(Dense(704,activation="relu"))
    model1.add(Dense(1408,activation="relu"))
    model1.add(Dense(1200,activation="relu"))
    model1.add(Dense(600,activation="relu"))
    model1.add(Dense(455,activation="relu"))
    model1.add(Dense(280,activation="relu"))
    model1.add(Dense(int(sys.argv[1]), activation = softmax_by_christian))
    model1.compile(loss=js_divergence,optimizer="adam")
    hist = model1.fit(X,Y,epochs=int(sys.argv[5]),batch_size=150,sample_weight=weights,callbacks=[csv_logger])
    return model1

csv_logger = tf.keras.callbacks.CSVLogger('D:\Masterarbeit\Predictions\prediction'+sys.argv[0].split('_')[1].split('.')[0]+'_'+sys.argv[1]+'_'+sys.argv[2]+'_'+sys.argv[3]+'_'+sys.argv[4]+'_'+sys.argv[5]+'\\training.log', append = True, separator = '\t')
data = np.load(datapfad, 'r')

liste1 = np.load('D:\Masterarbeit\Daten\Liste_Train_Test_Split\zufallsliste'+str(sys.argv[4])+'.npy')
X = data[liste1,0:6804]
Y = data[liste1,6804:(6804+int(sys.argv[1]))]

weights = data[liste1,(6804+int(sys.argv[1])+51):(6804+int(sys.argv[1])+51+1)]
for i in range(0,weights.shape[0]):
	if weights[i,0] == 1:
		weights[i,0] = 1*int(sys.argv[3])
	elif weights[i,0] == 0:
		weights[i,0] = 1

model = train_model(X,Y,weights)
model.summary()
#save model summary
with open('D:\Masterarbeit\Predictions\prediction'+sys.argv[0].split('_')[1].split('.')[0]+'_'+sys.argv[1]+'_'+sys.argv[2]+'_'+sys.argv[3]+'_'+sys.argv[4]+'_'+sys.argv[5]+'\\model.summary.txt', 'w') as f:
	with redirect_stdout(f):
		model.summary()

X = data[:,0:6804]

preds = model.predict(X)
np.save('D:\Masterarbeit\Predictions\prediction'+sys.argv[0].split('_')[1].split('.')[0]+'_'+sys.argv[1]+'_'+sys.argv[2]+'_'+sys.argv[3]+'_'+sys.argv[4]+'_'+sys.argv[5]+'\prediction'+sys.argv[0].split('_')[1].split('.')[0]+'_'+sys.argv[1]+'_'+sys.argv[2]+'_'+sys.argv[3]+'_'+sys.argv[4]+'_'+sys.argv[5]+'.npy', preds)
