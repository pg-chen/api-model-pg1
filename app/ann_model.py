from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from keras import models, layers
import numpy as np
import pandas as pd
import app.preprocessing as pre

#載入模型
import pickle
import gzip
from keras.models import load_model
model = models.load_model('app/model/Ann_model.h5')
#讀取Standard_Model
with gzip.open('app/model/scANN.pgz', 'r') as f:
    sc_X = pickle.load(f)
    # print(sc_X)

def predict(rent_data):
    rental = np.array([pre.one_hot1(rent_data[0])+pre.one_hot2(rent_data[1])+rent_data[2:7]+pre.calculate_dis(rent_data[7],rent_data[8])])
    rental_std = sc_X.transform(rental)
    pred = model.predict(rental_std)[0][0]
    print("%.2f" % pred)
    return "%.2f" % pred
