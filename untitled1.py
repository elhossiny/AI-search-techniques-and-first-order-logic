# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:28:55 2021

@author: workstation
"""

import pandas as pd
dataset=pd.read_csv("iris.csv")
dataset.describe()











x=dataset['sepal.length'].value_counts()
import matplotlib.pyplot as plt
plt.pie(x)
plt.show() 

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 


import numpy as np
import matplotlib.pyplot as plt


# creating the dataset
data = {'C':20, 'C++':15, 'Java':30,
		'Python':35}
courses = list(data.keys())
values = list(data.values())

#fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(courses, values, color ='maroon',
		width = 0.4)

plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()

# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# sorting by first name
data.sort_values("First Name", inplace = True)

# dropping ALL duplicate values
data.drop_duplicates(subset ="First Name",
					keep = "first", inplace = True)

# displaying data
data







# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Taking care of missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = ' ', strategy = 'mean')
imputer = imputer.fit_transform(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])












