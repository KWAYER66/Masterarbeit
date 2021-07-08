import numpy as np
import tensorflow as tf
from numpy import genfromtxt
from numpy import savetxt
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Activation, Dropout, Conv1D, Flatten, GlobalMaxPooling1D, GlobalAveragePooling1D,Reshape, LSTM, Input
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
def train_model(X,Z,weights):
	input_layer = Input(shape = (X.shape[1]))
	dense1 = Dense(176,activation="relu")(input_layer)
	dense2 = Dense(704,activation="relu")(dense1)
	dense3 = Dense(1408,activation="relu")(dense2)
	dense4 = Dense(1200,activation="relu")(dense3)
	dense5 = Dense(600,activation="relu")(dense4)
	dense6 = Dense(455,activation="relu")(dense5)
	dense7 = Dense(280,activation="relu")(dense6)

	outputs1 = Dense(int(sys.argv[1]), activation = softmax_by_christian, name = 'pwm')(dense7)
	outputs2 = Dense(51, activation = 'softmax', name = 'zuordnung')(dense7)

	loss1 = 'mean_squared_error'
	#loss1 = kl_divergence_by_christian
	loss2 = 'categorical_crossentropy'


	losses = {
		'pwm': loss1,
		'zuordnung': loss2,
	}


	model = Model(inputs = input_layer, outputs = [outputs1, outputs2], name = 'functional_model')

	model.compile(loss = losses, optimizer = 'adam')

	model.fit(X,Z, epochs = int(sys.argv[5]), batch_size = 150, sample_weight=weights, callbacks=[csv_logger])
	return model

csv_logger = tf.keras.callbacks.CSVLogger('D:\Masterarbeit\Predictions\prediction'+sys.argv[0].split('_')[1].split('.')[0]+'_'+sys.argv[1]+'_'+sys.argv[2]+'_'+sys.argv[3]+'_'+sys.argv[4]+'_'+sys.argv[5]+'\\training.log', append = True, separator = '\t')
data = np.load(datapfad, 'r')

liste1 = np.load('D:\Masterarbeit\Daten\Liste_Train_Test_Split\zufallsliste'+str(sys.argv[4])+'.npy')
X = data[liste1,0:6804]
Y = data[liste1,6804:(6804+int(sys.argv[1]))]
Y2 = data[liste1,(6804+int(sys.argv[1])):(6804+int(sys.argv[1])+51)]
Z = {
	'pwm': Y,
	'zuordnung': Y2
}
weights = data[liste1,(6804+int(sys.argv[1])+51):(6804+int(sys.argv[1])+51+1)]
for i in range(0,weights.shape[0]):
	if weights[i,0] == 1:
		weights[i,0] = 1*int(sys.argv[3])
	elif weights[i,0] == 0:
		weights[i,0] = 1

model = train_model(X,Z,weights)
model.summary()
#save model summary
with open('D:\Masterarbeit\Predictions\prediction'+sys.argv[0].split('_')[1].split('.')[0]+'_'+sys.argv[1]+'_'+sys.argv[2]+'_'+sys.argv[3]+'_'+sys.argv[4]+'_'+sys.argv[5]+'\\model.summary.txt', 'w') as f:
	with redirect_stdout(f):
		model.summary()

X = data[:,0:6804]

preds = model.predict(X)
np.save('D:\Masterarbeit\Predictions\prediction'+sys.argv[0].split('_')[1].split('.')[0]+'_'+sys.argv[1]+'_'+sys.argv[2]+'_'+sys.argv[3]+'_'+sys.argv[4]+'_'+sys.argv[5]+'\prediction'+sys.argv[0].split('_')[1].split('.')[0]+'_'+sys.argv[1]+'_'+sys.argv[2]+'_'+sys.argv[3]+'_'+sys.argv[4]+'_'+sys.argv[5]+'.npy', preds[0])
np.save('D:\Masterarbeit\Predictions\prediction'+sys.argv[0].split('_')[1].split('.')[0]+'_'+sys.argv[1]+'_'+sys.argv[2]+'_'+sys.argv[3]+'_'+sys.argv[4]+'_'+sys.argv[5]+'\zuordnung'+sys.argv[0].split('_')[1].split('.')[0]+'_'+sys.argv[1]+'_'+sys.argv[2]+'_'+sys.argv[3]+'_'+sys.argv[4]+'_'+sys.argv[5]+'.npy', preds[1])
