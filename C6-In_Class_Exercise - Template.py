# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 09:39:36 2020

@author: wchen
"""
# In[1]:
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Importing the dataset
os.chdir("C:/Users/wchen/Downloads")
dataset = pd.read_csv('MobilePrice.csv')
dataset.head(10)

print(dataset.columns)


# In[2]:
# Changing pandas dataframe to numpy array
X = dataset.iloc[:,0:20].values
y = dataset.iloc[:,20].values

# In[3]:
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# In[4]:
#Normalizing the data
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
print('Training data:')
print(X_train[0,])

X_test = sc_X.transform(X_test)
print('Test data:')
print(X_test[0,])

# In[5]:
# Part 2 - Now let's make the ANN!
import keras
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(16, input_dim=, activation=''))
model.add(Dense(12, activation=''))
model.add(Dense(4, activation=''))

model.compile(loss='', optimizer='', metrics=[''])

model.fit(X_train, y_train, epochs=100, batch_size=64)

# In[6]:
# Part 3 - Making predictions and evaluating the model

# Predicting the Test set results
y_pred = model.predict(X_test)

#Converting predictions to label
pred = list()
for i in range(len(y_pred)):
    pred.append(np.argmax(y_pred[i]))
    
# Calculate Prediction Accuracy    
from sklearn.metrics import accuracy_score
a = accuracy_score(y_test, pred)
print('Accuracy is:', a*100)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, pred)
print(cm)

# In[7]:
# Make some plots

model = Sequential()
model.add(Dense(16, input_dim=20, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(4, activation='softmax'))
model.compile(loss='', optimizer='', metrics=[''])
history = model.fit(X_train, y_train, validation_data = (X_test, y_test), epochs=100, batch_size=64)


plt.plot(history.history['sparse_categorical_accuracy'])
plt.plot(history.history['val_sparse_categorical_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()
