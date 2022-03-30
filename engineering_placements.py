import numpy as np
import pandas as pd
import os
import seaborn as sns
import pickle 
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
#from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score


df = pd.read_csv("collegePlace.csv")

le = preprocessing.LabelEncoder()
df["Gender"] = le.fit_transform(df["Gender"])

X=df[['Age', 'Gender', 'Internships', 'CGPA', 'Hostel',
       'HistoryOfBacklogs']]
y= df["PlacedOrNot"]

x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.30, random_state=100)


clff = RandomForestClassifier().fit(x_train,y_train)
prdd = clff.predict(x_test)

accr = accuracy_score(y_test, prdd)

pickle_out = open("classifier.pkl", mode = "wb") 
pickle.dump(clff, pickle_out) 
pickle_out.close()

print(accr)
