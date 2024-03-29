# -*- coding: utf-8 -*-
"""wine prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14u04SkdSbuUqXYu5JRD7xPHL0ptgSPcn
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

wine_dataset = pd.read_csv('/content/winequality-red.csv')

"""# New Section"""

#Number of Rows and Columns in the dataset
wine_dataset.shape

#First 5 rows of the Dataset
wine_dataset.head()

#Checking for missing values in the dataset
wine_dataset.isnull().sum

"""Data Analysis and Visualisation"""

#Statistical measures of the dataset
wine_dataset.describe()

#Number of values for each quality
sns.catplot(x='quality',data = wine_dataset, kind='count')

#Volatile Acidity Vs Quality
plot = plt.figure(figsize=(5,5))
sns.barplot(x='quality', y='volatile acidity', data = wine_dataset)

#Citric Acid Vs Quality
plot = plt.figure(figsize=(5,5))
sns.barplot(x='quality', y='citric acid', data = wine_dataset)

"""Correlation"""

correlation = wine_dataset.corr()

#Constructing a heatmap to understand the correlation between the columns
plt.figure(figsize=(10,10))
sns.heatmap(correlation,cbar=Tru, square=True, fmt = '.1f', annot=True, annot_kws{'size':8}, cmap='Blues')

"""Data Processing"""

#Seperate Data and Label
X = wine_dataset.drop('quality',axis=1)

print(X)

"""Label Binarization"""

Y =  wine_dataset['quality'].apply(lambda y_value: 1 if y_value >=7 else 0)

print(Y)

"""Train & Test Split"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

print(Y.shape, Y_train.shape, Y_test.shape)

"""Model Training: 
Random Foresr Classifier
"""

model = RandomForestClassifier()

model.fit(X_train,Y_train)

"""Model Evaluation

Accuracy Score
"""

# Accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy: ', test_data_accuracy)

"""Building a Predictive System"""

input_data = (7.3,0.65,0.0,1.2,0.065,15.0,21.0,0.9946,3.39,0.47,10.0)

#Changing the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

#Reshape the data as we are predicting the label for only one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]==1):
  print('Good Quality Wine')
else:
  print('Bad Quality Wine')

print(prediction)