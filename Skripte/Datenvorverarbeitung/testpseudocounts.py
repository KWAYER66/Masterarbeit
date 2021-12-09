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

dataohne = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz\AlignmentsPWMs_Zuordnung_Weights_Abst_tf.npy')[:,6804:6804+176]
data001 = np.load('D:\Masterarbeit\Daten\Input_NeuronalesNetz3\AlignmentsPWMs_Zuordnung_Weights_Abst_tf.npy')[:,6804:6804+176]

print(dataohne[0,72:108])
print(data001[0,72:108])
