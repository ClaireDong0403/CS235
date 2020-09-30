import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import scale, StandardScaler
from sklearn.metrics import confusion_matrix
import  pandas  as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn import neighbors
from sklearn import tree
import random

########################################################################################################################
## Preprocessing
########################################################################################################################
# read data from json file
bizData = pd.read_json('yelp_academic_dataset_business.json', lines=True)
# drop useless columns
bizData.drop(bizData.columns[[0,2,6,7,8, 10]], axis=1, inplace=True)
# convert attribute to numerical data
resData = pd.DataFrame()
for i in range(0, len(bizData)):
    if 'Restaurants' in bizData['categories'][i]:
        resData = resData.append(bizData.loc[i])
attributes = ['Alcohol',
              'Ambience',
              'BikeParking',
              'BusinessParking',
              'DietaryRestrictions',
              'DogsAllowed',
              'GoodForKids',
              'HappyHour',
              'HasTV',
              'OutdoorSeating',
              'RestaurantsAttire',
              'RestaurantsPriceRange2',
              'RestaurantsReservations',
              'WiFi']

counter = 0
for i in range(0, len(resData)):

    ats = [i.split(':', 1)[0] for i in resData['attributes'][i]]
    contain = [i for i in ats if i in attributes]

    if len(contain) == len(attributes):
        counter += 1

resData2 = pd.DataFrame()
counter = 0
for i in range(0, len(resData)):

    ats = [i.split(':', 1)[0] for i in resData['attributes'][i]]
    contain = [i for i in ats if i in attributes]

    if len(contain) == len(attributes):
        counter += 1
        resData2 = resData2.append(resData.loc[i])
attributes = ['Alcohol',
              'ambRomantic',
              'ambIntimate',
              'ambClassy',
              'ambHipster',
              'ambDivey',
              'ambTouristy',
              'ambTrendy',
              'ambUpscale',
              'ambCasual',
              'BikeParking',
              'BusinessParking',
              'DietaryRestrictions',
              'DogsAllowed',
              'GoodForKids',
              'HappyHour',
              'HasTV',
              'OutdoorSeating',
              'RestaurantsAttire',
              'RestaurantsPriceRange2',
              'RestaurantsReservations',
              'WiFi']

newFeatures = pd.DataFrame(0, index=np.arange(len(resData2)), columns=attributes)

########################################################################################################################
## SVM
########################################################################################################################
# feature
feature = []
# label
label = []
# split train set and test set
X_train,X_test, Y_train, Y_test = train_test_split(feature,label,test_size=0.2, random_state=0)
# norm
min_max_scaler = preprocessing.MinMaxScaler()

X_train = min_max_scaler.fit_transform(X_train)
X_test = min_max_scaler.transform(X_test)

########################################################################################################################
# GridSearch cg
########################################################################################################################
parameters = { 'C': np.linspace(0.0001,100,50), 'gamma': np.linspace(0.0001,100,50)}
svr = svm.SVC('rbf')
clf = GridSearchCV(svr, parameters, cv=5)
clf.fit(X_train, Y_train)
cv_result = pd.DataFrame.from_dict(clf.cv_results_)
with open('cv_result.csv', 'w') as f:
    cv_result.to_csv(f)

print('The parameters of the best model are: ')
print(clf.best_params_)


########################################################################################################################
## SVM rbf
########################################################################################################################
classifier = svm.SVC(C=clf.best_params_['C'],kernel='rbf',gamma=clf.best_params_['gamma']) # SVM
classifier.fit(X_train,Y_train) #train

# calculate accuracy
print("SVM(rbf)train set：",classifier.score(X_train,Y_train))
print("SVM(rbf)test set：",classifier.score(X_test,Y_test))

########################################################################################################################
## SVM linear
########################################################################################################################
classifier = svm.SVC(kernel='linear') # SVM
classifier.fit(X_train,Y_train) #train

# calculate accuracy
print("SVM(linear)训练集：",classifier.score(X_train,Y_train))
print("SVM(linear)测试集：",classifier.score(X_test,Y_test))