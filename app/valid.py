import numpy as np
import pandas as pd
import app.preprocessing as pre
import app.regression_model as reg
import app.ann_model as ann
import app.RF_model as rf
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle
import gzip
#匯入資料、選擇欄位
dataset = pd.read_csv("../處理檔案/2019_valid3.csv")
dataset = dataset[0:30001]
X = dataset.iloc[:, 3:22].values
y = dataset.iloc[:, -1].values
y = y.reshape(-1,1)

#物件類別
ct=ColumnTransformer([('District',OneHotEncoder(),[1])],remainder='passthrough')
X=np.array(ct.fit_transform(X), dtype='float64')
X = X[:, 1:]

#行政區
# X[:, 12] = labelencoder_X.fit_transform(X[:, 12])
ct=ColumnTransformer([('Object',OneHotEncoder(),[2])],remainder='passthrough')
X=np.array(ct.fit_transform(X), dtype='float64')
X = X[:, 1:]

#LR 特徵選取
X_LR = X[:,[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
        17, 19, 20, 21, 22, 24, 25, 26, 27, 28]]

#LR切割訓練與測試資料
# X_LRtrain, X_LRtest, y_train, y_test = train_test_split(X_LR, y, test_size = 0.2, random_state = 0)

#標準化
# sc_X = StandardScaler()
# X_LRtrain = sc_X.fit_transform(X_LRtrain)
# X_LRtest = sc_X.transform(X_LRtest)

#載入模型
#讀取Standard_Model
with gzip.open('app/model/Standard_scaler.pgz', 'r') as f:
    sc_X = pickle.load(f)
#讀取Regression_Model
with gzip.open('app/model/Regression_model.pgz', 'r') as f:
    Regression = pickle.load(f)
    # print(Regression)
X_std = sc_X.transform(X_LR)

#預測
result1 = Regression.predict(X_std)


#切割訓練與測試資料
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#標準化
# scANN_X = StandardScaler()
# X_ANNtrain = scANN_X.fit_transform(X_train)
# X_ANNtest = scANN_X.transform(X_test)

#ANN
from keras import models
from keras.models import load_model
model = models.load_model('app/model/Ann_model.h5')
#讀取Standard_Model
with gzip.open('app/model/scANN.pgz', 'r') as f:
    scANN_X = pickle.load(f)

X_ANNstd = scANN_X.transform(X)
#預測
result2 = model.predict(X_ANNstd)

#RF
#讀取RandomForest_Model
with gzip.open('app/model/RandomForest_model_100.pgz', 'rb') as f:
    randomforest = pickle.load(f)

result3 = randomforest.predict(X)
result3 = result3.reshape(-1,1)

result = []
for i in range(len(result1)):
    result.append((result1[i][0] + result2[i][0]) * 0.30 + result3[i][0] * 0.4)

#驗證
from sklearn.metrics import mean_squared_error
MSE1 = mean_squared_error(y, result1)
RMSE1 = np.sqrt(MSE1)
print('Linear Regression_MSE:',MSE1)
print('Linear Regression_RMSE:',RMSE1)

#驗證
MSE2 = mean_squared_error(y, result2)
RMSE2 = np.sqrt(MSE2)
print('ANN_MSE:',MSE2)
print('ANN_RMSE:',RMSE2)

#驗證
MSE3 = mean_squared_error(y, result3)
RMSE3 = np.sqrt(MSE3)
print('RandomForest_MSE:',MSE3)
print('RandomForest_RMSE:',RMSE3)

#驗證
MSE = mean_squared_error(y, result)
RMSE = np.sqrt(MSE)
print('Average_MSE:',MSE)
print('Average_MSE:',RMSE)



