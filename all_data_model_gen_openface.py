#!/usr/bin/env python


# # LOAD

# In[1]:


task_name = 'all_data'


# In[2]:


model_path = './models/{0}/'.format(task_name)


# In[3]:


import os
import numpy as np
import pandas as pd
import warnings
import pickle

from tqdm import tqdm


# In[4]:


save_path = './data/tmp_analysis/{0}'.format(task_name)
save_train_path = save_path + '_train.csv'
save_test_path = save_path + '_test.csv'
save_valid_path = save_path + '_valid.csv'


Train = pd.read_csv(save_train_path)
Test = pd.read_csv(save_test_path)
Valid = pd.read_csv(save_valid_path)


# In[5]:


X = Train.to_numpy()[:,3:]


# In[6]:


del Train


# In[7]:


Xtest = Test.to_numpy()[:,3:]


# In[8]:


del Test


# In[9]:


Xvalid = Valid.to_numpy()[:,3:]


# In[10]:


del Valid



import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"] = ""

import keras
from keras import layers

import matplotlib.pyplot as plt


# In[21]:


print(X.shape)


# In[22]:


input_dim = X.shape[1]
encoding_dim = 32

input_layer = keras.Input(shape=(input_dim,))
encoded_layer = layers.Dense(encoding_dim, activation='relu')(input_layer)
decoded_layer = layers.Dense(input_dim, activation='relu')(encoded_layer)

autoencoder_32 = keras.Model(input_layer,decoded_layer)

encoder_32 = keras.Model(input_layer, encoded_layer)


# In[23]:


autoencoder_32.compile(optimizer='adam',
                    loss='binary_crossentropy')


# In[24]:


autoencoder_32.summary()


# In[ ]:


history = autoencoder_32.fit(X, X, epochs=2, batch_size=64, verbose=1, validation_data=(Xtest, Xtest))


# In[ ]:


fig, ax = plt.subplots()

plt.plot([0]+history.history['loss'], label='train')
plt.plot([0]+history.history['val_loss'], label='test')
plt.legend()
plt.show()


# In[ ]:


predictions = autoencoder_32.predict(Xvalid)
# TODO I should probably do something with the validation set


# In[ ]:


autoencoder_32.save(model_path + 'autoencoder_32.pb')
encoder_32.save(model_path + 'encoder_32.pb')


# 18 wide encoder

# In[ ]:


import keras
from keras import layers


# In[ ]:


X = Train.to_numpy()[:,3:]
Xtest = Test.to_numpy()[:,3:]
Xvalid = Valid.to_numpy()[:,3:]


# In[ ]:


input_dim = X.shape[1]
encoding_dim = 18

input_layer = keras.Input(shape=(input_dim,))
encoded_layer = layers.Dense(encoding_dim, activation='relu')(input_layer)
decoded_layer = layers.Dense(input_dim, activation='relu')(encoded_layer)

autoencoder_18 = keras.Model(input_layer,decoded_layer)

encoder_18 = keras.Model(input_layer, encoded_layer)


# In[ ]:


autoencoder_18.compile(optimizer='adam',
                    loss='binary_crossentropy')


# In[ ]:


autoencoder_18.summary()


# In[ ]:


history = autoencoder_18.fit(X, X, epochs=2, batch_size=64, verbose=0, validation_data=(Xtest, Xtest))


# In[ ]:


fig, ax = plt.subplots()

plt.plot([0]+history.history['loss'], label='train')
plt.plot([0]+history.history['val_loss'], label='test')
plt.legend()
plt.show()


# In[ ]:


predictions = autoencoder_5.predict(Xvalid)
# TODO I should probably do something with the validation set


# In[ ]:


autoencoder_18.save(model_path + 'autoencoder_18.pb')
encoder_18.save(model_path + 'encoder_18.pb')
