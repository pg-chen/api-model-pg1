from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import math
import pandas as pd
import app.preprocessing as pre
#載入模型
import pickle
import gzip


#讀取RandomForest_Model
with gzip.open('app/model/RandomForest_model_100.pgz', 'rb') as f:
    randomforest = pickle.load(f)
    #print(Regression)

# randomforest = load('app/model/RandomForest_model.joblib') 

def predict(rent_data):
    rental = np.array([pre.one_hot1(rent_data[0])+pre.one_hot2(rent_data[1])+rent_data[2:7]+pre.calculate_dis(rent_data[7],rent_data[8])])
    pred = randomforest.predict(rental)[0]
    print("%.2f" % pred)
    return "%.2f" % pred
