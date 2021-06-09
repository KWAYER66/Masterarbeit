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


#sys.argv[1] -> data path
#sys.argv[2] -> 176 für ALLE, 140 für Gruppe
sp = str(sys.argv[2])
#sys.argv[3] -> Index für Speicher
sp1 = str(sys.argv[3])
#sys.argv[4] -> Faktor sample_weights
sp2 = str(sys.argv[4])
#sys.argv[5] -> #epochs
sp3 = str(sys.argv[5])

print('Einstellungen sind: '+sp+sp1+sp2+sp3)
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
def build_model(X,Z,weights):
	input_layer = Input(shape = (X.shape[1]))
	dense1 = Dense(27,activation="relu")(input_layer)
	dense2 = Dense(int(sys.argv[2]),activation="relu")(dense1)
	dense3 = Dense(54,activation="relu")(dense2)
	dense4 = Dense(108,activation="relu")(dense3)

	outputs1 = Dense(int(sys.argv[2]), activation = softmax_by_christian, name = 'pwm')(dense4)
	outputs2 = Dense(units = '51', activation = 'softmax', name = 'zuordnung')(input_layer)

	#loss1 = 'mean_squared_error'
	loss1 = kl_divergence_by_christian
	loss2 = 'categorical_crossentropy'


	losses = {
		'pwm': loss1,
		'zuordnung': loss2,
	}


	model = Model(inputs = input_layer, outputs = [outputs1, outputs2], name = 'functional_model')

	model.compile(loss = losses, optimizer = 'adam')

	model.fit(X,Z, epochs = int(sys.argv[5]), batch_size = 150, sample_weight=weights, callbacks=[csv_logger])
	return model


#Save log datei
csv_logger = tf.keras.callbacks.CSVLogger('training_Multiple_Outputs.log', append = True)

#Load Input Data
data = np.load(sys.argv[1], 'r')
rng = default_rng()
liste1 = rng.choice(range(0,len(data)), size =1500, replace = False)
#liste1 = range(0,data.shape[0])
X = data[liste1,0:6804]
Y = data[liste1,6804:(6804+int(sys.argv[2]))]
Y2 = data[liste1,(6804+int(sys.argv[2])):(6804+int(sys.argv[2])+51)]
Z = {
	'pwm': Y,
	'zuordnung': Y2
}
#Faktor für weights
weights = data[liste1,(6804+int(sys.argv[2])+51):(6804+int(sys.argv[2])+51+1)]
for i in range(0,weights.shape[0]):
	if weights[i,0] == 1:
		weights[i,0] = float(sys.argv[4])
	elif weights[i,0] == 0:
		weights[i,0] = 1

#Train
model = build_model(X,Z,weights)
model.summary()
#Predict
X = data[:,0:6804]
preds = model.predict(X)

#Save Predictions
if os.path.exists('D:\Inferenz_von_TF_Bindepraeferenzen\Predictions_PWMSNetz5_Multiple_Outputs') == False:
	os.makedirs('D:\Inferenz_von_TF_Bindepraeferenzen\Predictions_PWMSNetz5_Multiple_Outputs')
np.save('D:\Inferenz_von_TF_Bindepraeferenzen\Predictions_PWMSNetz5_Multiple_Outputs\predictions'+sp+'_'+sp1+'_'+sp2+'_'+sp3+'.npy', preds[0])

#TEST, Umwandlung der KL-Divergence für die Zuordnungen in ein Maß für die Sicherheit der Schätzung der Zuordnungen
arr = tf.convert_to_tensor(np.full((1,51), 1/51), np.float32)
arr2 = np.full((1,51),0)
arr2[0,5] = 1
arr3 = tf.convert_to_tensor(arr2, np.float32)
kl_div = kl_divergence_by_christian(arr,arr3)
kl_div100Prozenz = float(np.asarray(kl_div[0,]))

ausgabearr = np.empty(shape = (data.shape[0],1))

for i in range(0,preds[1].shape[0]):
  wrs = kl_divergence_by_christian(arr,preds[1][i,])
  ausgabearr[i,0] = float(np.asarray(wrs[0,]))/kl_div100Prozenz

#Save Maß für Sicherheit der Schätzung
np.save('D:\Inferenz_von_TF_Bindepraeferenzen\Predictions_PWMSNetz5_Multiple_Outputs\predictions_zuordnung'+sp+'_'+sp1+'_'+sp2+'_'+sp3+'.npy', ausgabearr)
print(np.mean(ausgabearr))
