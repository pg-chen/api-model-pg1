from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import math
import pandas as pd


def one_hot1(Dis):
    District = [0,0,0,0,0,0,0,0,0,0,0]
    
    if Dis == 1:
        return District
    else:
        District[Dis-2] = 1
        return District

def one_hot2(Obj):
    Object = [0,0]
    
    if Obj == 0:
        return Object
    else:
        Object[Obj-1] = 1
        return Object
# 計算距離
def getDistance(latA, lonA, latB, lonB):
    ra = 6378140  # 赤道半徑
    rb = 6356755  # 極半徑
    flatten = (ra - rb) / ra  # Partial rate of the earth
    # change angle to radians
    radLatA = math.radians(latA)
    radLonA = math.radians(lonA)
    radLatB = math.radians(latB)
    radLonB = math.radians(lonB)
    pA = math.atan(rb / ra * math.tan(radLatA))
    pB = math.atan(rb / ra * math.tan(radLatB))
    x = math.acos(math.sin(pA) * math.sin(pB) + math.cos(pA) * math.cos(pB) * math.cos(radLonA - radLonB))
    c1 = (math.sin(x) - x) * (math.sin(pA) + math.sin(pB)) ** 2 / math.cos(x / 2) ** 2
    c2 = (math.sin(x) + x) * (math.sin(pA) - math.sin(pB)) ** 2 / math.sin(x / 2) ** 2
    dr = flatten / 8 * (c1 - c2)
    distance = ra * (x + dr)
    distance = round(distance / 1000, 4)
    return f'{distance}'

#loading data
hospital = pd.read_csv("app/location_dataset/hospital.csv")
market = pd.read_csv("app/location_dataset/market.csv")
park = pd.read_csv("app/location_dataset/park.csv")
school_1 = pd.read_csv("app/location_dataset/Kindergarten.csv")
school_2 = pd.read_csv("app/location_dataset/elementary.csv")
school_3 = pd.read_csv("app/location_dataset/junior.csv")
shop = pd.read_csv("app/location_dataset/shop.csv")
metro = pd.read_csv("app/location_dataset/metro.csv")
temple = pd.read_csv("app/location_dataset/temple.csv")
sewage = pd.read_csv("app/location_dataset/sewage.csv")
trash = pd.read_csv("app/location_dataset/trash.csv")
funeral = pd.read_csv("app/location_dataset/funeral.csv")

def calculate_dis_linear(rent_lat,rent_lnt):
    hos_dis ,market_dis ,park_dis, school1_dis, school2_dis, school3_dis, department_dis, metro_dis, \
    temple_dis, sewage_dis, trash_dis, funeral_dis = [],[],[],[],[],[],[],[],[],[],[],[]
    # for i in range(len(hospital)):
    #     hos_dis.append(float(getDistance(rent_lat,rent_lnt,float(hospital['lat'][i]),float(hospital['lnt'][i]))))
    for i in range(len(market)):
        market_dis.append(float(getDistance(rent_lat,rent_lnt,float(market['lat'][i]),float(market['lnt'][i]))))
    for i in range(len(park)):
        park_dis.append(float(getDistance(rent_lat,rent_lnt,float(park['lat'][i]),float(park['lnt'][i]))))
    for i in range(len(school_1)):
        school1_dis.append(float(getDistance(rent_lat,rent_lnt,float(school_1['lat'][i]),float(school_1['lnt'][i]))))
    for i in range(len(school_2)):
        school2_dis.append(float(getDistance(rent_lat,rent_lnt,float(school_2['lat'][i]),float(school_2['lnt'][i]))))
    # for i in range(len(school_3)):
    #     school3_dis.append(float(getDistance(rent_lat,rent_lnt,float(school_3['lat'][i]),float(school_3['lnt'][i]))))
    for i in range(len(shop)):
        department_dis.append(float(getDistance(rent_lat,rent_lnt,float(shop['lat'][i]),float(shop['lnt'][i]))))
    for i in range(len(metro)):
        metro_dis.append(float(getDistance(rent_lat,rent_lnt,float(metro['lat'][i]),float(metro['lnt'][i]))))
    for i in range(len(temple)):
        temple_dis.append(float(getDistance(rent_lat,rent_lnt,float(temple['lat'][i]),float(temple['lnt'][i]))))
    for i in range(len(sewage)):
        sewage_dis.append(float(getDistance(rent_lat,rent_lnt,float(sewage['lat'][i]),float(sewage['lnt'][i]))))
    for i in range(len(trash)):
        trash_dis.append(float(getDistance(rent_lat,rent_lnt,float(trash['lat'][i]),float(trash['lnt'][i]))))
    # for i in range(len(funeral)):
    #     funeral_dis.append(float(getDistance(rent_lat,rent_lnt,float(funeral['lat'][i]),float(funeral['lnt'][i]))))
    return [min(market_dis),min(park_dis),min(school1_dis),min(school2_dis),min(department_dis),min(metro_dis),min(temple_dis),min(sewage_dis),min(trash_dis)]
    # return [min(hos_dis),min(market_dis),min(park_dis),min(school1_dis),min(school2_dis),min(school3_dis),min(department_dis),min(metro_dis),min(temple_dis),min(sewage_dis),min(trash_dis),min(funeral_dis)]


def calculate_dis(rent_lat,rent_lnt):
    hos_dis ,market_dis ,park_dis, school1_dis, school2_dis, school3_dis, department_dis, metro_dis, \
    temple_dis, sewage_dis, trash_dis, funeral_dis = [],[],[],[],[],[],[],[],[],[],[],[]
    for i in range(len(hospital)):
        hos_dis.append(float(getDistance(rent_lat,rent_lnt,float(hospital['lat'][i]),float(hospital['lnt'][i]))))
    for i in range(len(market)):
        market_dis.append(float(getDistance(rent_lat,rent_lnt,float(market['lat'][i]),float(market['lnt'][i]))))
    for i in range(len(park)):
        park_dis.append(float(getDistance(rent_lat,rent_lnt,float(park['lat'][i]),float(park['lnt'][i]))))
    for i in range(len(school_1)):
        school1_dis.append(float(getDistance(rent_lat,rent_lnt,float(school_1['lat'][i]),float(school_1['lnt'][i]))))
    for i in range(len(school_2)):
        school2_dis.append(float(getDistance(rent_lat,rent_lnt,float(school_2['lat'][i]),float(school_2['lnt'][i]))))
    for i in range(len(school_3)):
        school3_dis.append(float(getDistance(rent_lat,rent_lnt,float(school_3['lat'][i]),float(school_3['lnt'][i]))))
    for i in range(len(shop)):
        department_dis.append(float(getDistance(rent_lat,rent_lnt,float(shop['lat'][i]),float(shop['lnt'][i]))))
    for i in range(len(metro)):
        metro_dis.append(float(getDistance(rent_lat,rent_lnt,float(metro['lat'][i]),float(metro['lnt'][i]))))
    for i in range(len(temple)):
        temple_dis.append(float(getDistance(rent_lat,rent_lnt,float(temple['lat'][i]),float(temple['lnt'][i]))))
    for i in range(len(sewage)):
        sewage_dis.append(float(getDistance(rent_lat,rent_lnt,float(sewage['lat'][i]),float(sewage['lnt'][i]))))
    for i in range(len(trash)):
        trash_dis.append(float(getDistance(rent_lat,rent_lnt,float(trash['lat'][i]),float(trash['lnt'][i]))))
    for i in range(len(funeral)):
        funeral_dis.append(float(getDistance(rent_lat,rent_lnt,float(funeral['lat'][i]),float(funeral['lnt'][i]))))
    # return [min(market_dis),min(park_dis),min(school1_dis),min(school2_dis),min(department_dis),min(metro_dis),min(temple_dis),min(sewage_dis),min(trash_dis)]
    return [min(hos_dis),min(market_dis),min(park_dis),min(school1_dis),min(school2_dis),min(school3_dis),min(department_dis),min(metro_dis),min(temple_dis),min(sewage_dis),min(trash_dis),min(funeral_dis)]
