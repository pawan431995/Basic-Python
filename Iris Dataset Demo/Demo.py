import sys
import scipy
import matplotlib
import numpy
import pandas
import sklearn
''''
print("python sys ",sys.version)
print("python scipy ",scipy.version)
print("python",matplotlib.__version__)
print("python",numpy.__version__)
print("python",pandas.__version__)
print("python",sklearn.__version__)

'''

import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from  sklearn.linear_model import logistic_regression_path
from sklearn.tree import DecisionTreeClassifier
from  sklearn.neighbors import KNeighborsClassifier
from  sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


#url="irisdata.csv"
#url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
url="C:/Users/Administrator/Desktop/python/irisdata.csv"
names=["sepal-length","sepal-width","petal-length","petal-width","class"]
dataset=pandas.read_csv(url, sep=",",engine='python')
#dataset=pandas.read_csv(url,names)
'''
print(dataset.shape)
print(dataset.head(30))
print(dataset.describe())
print(dataset.groupby('class').size())'''
#dataset.plot(kind='box',subplots=True,layout=(2,2),sharex=False,sharey=False)

#dataset.hist()
#scatter_matrix(dataset)
#plt.show()

array=dataset.values
x=array[:,0:4]
y=array[:,4]
validation_size=0.20
seed=6
X_train, X_test,Y_train,Y_test=model_selection.train_test_split(x,y,test_size=validation_size,random_state=seed)
seed=6
scoring='accuracy'

model=[]
model.append(('NB',GaussianNB()))
model.append(('CART',DecisionTreeClassifier()))
model.append(('KNC',KNeighborsClassifier()))
#model.append(('linalg',linalg()))
result=[]
name=[]
for name,model1 in model:
    kfold=model_selection.KFold(n_splits=10,random_state=seed)
    cv_result=model_selection.cross_val_score(model1,X_train,Y_train,cv=kfold,scoring=scoring)
    result.append(cv_result)
    print(name,cv_result.mean(),cv_result.std())







