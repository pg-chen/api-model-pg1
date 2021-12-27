from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import pandas as pd
import app.preprocessing as pre
# rent_data = [10,1,1,5,9,13.3,10,25.0570704, 121.5268284]

#載入模型
import pickle
import gzip

#讀取Standard_Model
with gzip.open('app/model/Standard_scaler.pgz', 'r') as f:
    sc_X = pickle.load(f)
    # print(sc_X)
#讀取Regression_Model
with gzip.open('app/model/Regression_model.pgz', 'r') as f:
    Regression = pickle.load(f)
    # print(Regression)

def predict(rent_data):
    rental = np.array([pre.one_hot1(rent_data[0])+pre.one_hot2(rent_data[1])+rent_data[2:7]+pre.calculate_dis_linear(rent_data[7],rent_data[8])])
    rental_std = sc_X.transform(rental)
    pred = Regression.predict(rental_std)[0][0]
    print("%.2f" % pred)
    return "%.2f" % pred
