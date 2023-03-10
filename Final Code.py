# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 00:48:41 2022

@author: 9941064513.UPS
"""
import pandas as pd
import numpy as np
from datetime import date
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeRegressor
import statsmodels.api as sm
import sklearn.metrics as ms


df = pd.read_csv("Crypto.csv")
df2=df.drop(["Number", "Timestamp"], axis = 1)

df2['Date'] = pd.to_numeric(df2.Date.str.replace('/',''))

# Move Middle column to the Begining
df2 = pd.DataFrame(df2)
temp_cols=df2.columns.tolist()
index=df2.columns.get_loc("MarketCap")
new_cols=temp_cols[index:index+1] + temp_cols[0:index] + temp_cols[index+1:]
df2=df2[new_cols]

print(df2.info())
print(df2.isnull().sum())

X = df2.iloc [:,1:].values
y = df2.iloc [:,0].values


# Lable Encoder for independent Value X

labelencoder = LabelEncoder()
X[:,-2] = labelencoder.fit_transform(X[:,-2])


#Spliting the dataset

X_train,X_test, y_train,y_test = train_test_split(X,y,test_size= 0.2, random_state=42)

#Apply the linear Regrission for Crypto dataset

linearregression = LinearRegression()
linearregression.fit(X_train, y_train)

y_pred = linearregression.predict(X_test)

#Standarization 

standardscaler = StandardScaler()

X_train = standardscaler.fit_transform(X_train)
X_test = standardscaler.fit_transform(X_test)

#Training the RandomForest Regression model on the whole dataset

regressor = RandomForestRegressor(n_estimators = 40, random_state = 42)
regressor.fit(X_train, y_train)

y_pred1=regressor.predict(X_test)

print('explained_variance_score for random forest',ms.explained_variance_score(y_test, y_pred1))


#Training the Decision Tree Regression model on the whole dataset
reg= DecisionTreeRegressor(random_state = 42)
reg.fit(X_train, y_train)

# Predicting a new result
y_pred3=reg.predict(X_test)

print('explained_variance_score desision tree',ms.explained_variance_score(y_test, y_pred3))

# Support Vector Classification
#from sklearn.svm import SVC
#SVm=SVC()
#SVm.fit(X_train,y_train)
#y_pred_SVm=SVm.predict(X_test)

 
#print('explained_variance_score for Support Vector Classification',ms.explained_variance_score(y_test, y_pred_SVm))
