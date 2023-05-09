# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 09:32:32 2021

@author: workstation
"""
# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
ct=ColumnTransformer([('Country', OneHotEncoder(),[0])],remainder='passthrough')
X=ct.fit_transform(X)
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
#onehotencoder = OneHotEncoder(categorical_features = [0])
#X = onehotencoder.fit_transform(X).toarray()
# Encoding the Dependent Variable
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)


# fatorize 
dataset['Country'] = pd.factorize(dataset['Country'])[0]


dataset['fact'] = pd.factorize(dataset['Country'])[0]



