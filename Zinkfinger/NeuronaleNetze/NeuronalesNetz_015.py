import numpy as np
import tensorflow as tf
from numpy import genfromtxt
from numpy import savetxt
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import MaxPooling2D, Conv2D, Dense, Activation, Dropout, Conv1D, Flatten, GlobalMaxPooling1D, GlobalAveragePooling1D,Reshape, LSTM, Input
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
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import concatenate
from tensorflow.keras.datasets import mnist
from numpy import genfromtxt
print(tf.__version__)

if os.path.exists('D:\Masterarbeit\ZinkFinger\Predictions\prediction'+sys.argv[0].split('_')[1].split('.')[0]+'_'+str(sys.argv[1])+'_'+str(sys.argv[2])) == False:
	os.makedirs('D:\Masterarbeit\ZinkFinger\Predictions\prediction'+sys.argv[0].split('_')[1].split('.')[0]+'_'+str(sys.argv[1])+'_'+str(sys.argv[2]))
datapfad = 'D:\Masterarbeit\ZinkFinger\Input_NeuronalesNetzAlignment4.tsv'
#sys.argv[1] -> Anzahl an Epochen
#sys.argv[2] -> Bestimme Train/Test - Split

#sys.argv[2] -> Index der Iterationen zum Speichern der Datei
#sys.argv[3] -> Faktor fuer sample_weights
#sys.argv[4] -> Bestimme Train/Test - Split
#sys.argv[5] -> Anzahl an Epochen
def js_divergence(p, q):
	m = 0.5 * (p + q)
	return 0.5 * kl_divergence_by_christian(p, m) + 0.5 * kl_divergence_by_christian(q, m)
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
  y_true = y_true[:,20:180]

  y_true = backend.clip(y_true, backend.epsilon(), 1)
  y_pred = backend.clip(y_pred, backend.epsilon(), 1)


  y_pred2 = y_pred[:,0:160]
  for rev in range(0,2):
	  for i in range(0,40):
		  if i%4==0:
			  j = i + 160
			  y_pred2 = y_pred[:,i:j]
			  if rev == 1:
				  y_pred2 = tf.reverse(y_pred2, [-1])
			  if (rev == 0) & (i == 0):
				  min = tf.expand_dims(math_ops.reduce_sum(y_true * math_ops.log(y_true / y_pred2), axis=-1), -1)
			  else:
				  min2 = tf.expand_dims(math_ops.reduce_sum(y_true * math_ops.log(y_true / y_pred2), axis=-1), -1)
				  min = tf.concat([min, min2], axis = 1)
  newmin = tf.math.reduce_min(min, axis = 1)
  return newmin
def train_model(X,Y):
	input_layer = Input(shape = (X.shape[1], X.shape[2]), name='DBDs')
	Conv1_1 = Conv1D(filters = 20, kernel_size=1, strides = 1,activation="relu", input_shape=[X.shape[1],X.shape[2]])(input_layer)
	flatten1 = Flatten()(Conv1_1)
	outputs1 = Dense((200), activation = softmax_by_christian, name = 'pwm')(flatten1)
	model = Model(inputs = input_layer, outputs = outputs1, name = 'functional_model2')
	model.compile(loss = js_divergence, optimizer = 'adam')
	model.fit(X,Y, epochs = int(sys.argv[1]), batch_size = 150, callbacks=[csv_logger])
	return model

csv_logger = tf.keras.callbacks.CSVLogger('D:\Masterarbeit\ZinkFinger\Predictions\prediction'+sys.argv[0].split('_')[1].split('.')[0]+'_'+str(sys.argv[1])+'_'+str(sys.argv[2])+'\\training.log', append = True, separator = '\t')
data = genfromtxt(datapfad, delimiter="\t")
liste1 = np.load('D:\Masterarbeit\ZinkFinger\zufallsliste2\zufallsliste_neu'+str(sys.argv[2])+'.npy')
X = data[liste1,0:32076].astype(np.int)
X = X.reshape((-1,int(X.shape[1]/1188),1188))
Y = data[liste1,32076:32276].astype(np.float)

model = train_model(X,Y)
model.summary()
#save model summary
with open('D:\Masterarbeit\ZinkFinger\Predictions\prediction'+sys.argv[0].split('_')[1].split('.')[0]+'_'+str(sys.argv[1])+'_'+str(sys.argv[2])+'\\model.summary.txt', 'w') as f:
	with redirect_stdout(f):
		model.summary()

X = data[:,0:32076].astype(np.float)
X = X.reshape((-1,int(X.shape[1]/1188),1188))


preds = model.predict(X)
np.save('D:\Masterarbeit\ZinkFinger\Predictions\prediction'+sys.argv[0].split('_')[1].split('.')[0]+'_'+str(sys.argv[1])+'_'+str(sys.argv[2])+'\\pwms.npy', preds)
print(preds)
