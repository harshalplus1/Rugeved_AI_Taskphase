#%%
from turtle import color
from numpy import mean
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
#preprocessing data
data=pd.read_csv(r'/home/harshal/Downloads/train.csv')
print(data.info())
#cleaning
#checking if null values are present
print(data.isnull().sum())

print(data.describe())

print(data.dtypes['carat'])

#filling na values,if present
data.interpolate()
#1.feature engineering
#1.1 checking freequency of attributes
data.hist(bins=100,figsize=(20,15))
#1.2 checking the relations between each attribute
sns.pairplot(data)
#1.3 checking data correlation through heatmap with their annotations
#checking the attributes with target variable
sns.heatmap(data.corr(),annot=True)
d1=data.corr()
print(d1)
d1['price'].sort_values(ascending = False).plot(kind = 'bar');
#1.4 dropping depth as it has very poor relation with price
data=data.drop(columns=['depth'])
print(data)
#2.applying logistic regression
#2.1 getting dummy values for columns with string attributes
col=pd.get_dummies(data['color'])
ty=pd.get_dummies(data['cut'])
cla=pd.get_dummies(data['clarity'])
#2.2 dropping columns which have the least frequency
col=col.drop(['J'],axis=1)
cla=cla.drop(['I1'],axis=1)
ty=ty.drop(['Fair'],axis=1)
#2.3 concatenating new columns to data and dropping away the old ones
data=pd.concat([data,col,cla,ty],axis=1)
data=data.drop(['cut','color','clarity'],axis=1)
#2.4 Final data
print(data)
#3.0 splitting data into train and test
X=data.drop(['price'],axis=1)
y=data['price']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)
#3.1 creating an object clf of class LinearRegression
from sklearn.linear_model import LinearRegression
clf=LinearRegression()
#3.2 fitting the training results
clf.fit(X_train,y_train)
#3.3 predicting the test results of x 
y_pred=clf.predict(X_test)
y_train=clf.predict(X_train)
# print(clf.predict([[0.136542]]))
#3.4 comparing the prediction with actual values
#function to calculate slop and y intercept
def gradient(x,y):
     m=(((mean(x)*mean(y)-mean(x*y))/(mean(x)*mean(y)-mean(x*x))))
     b=mean(y)-m*mean(x)
     return m,b        
m1,b1=gradient(y_test,y_pred)
print(m1,b1)
#4.0 plotting linear regression line
plt.scatter(y_test,y_pred,s=0.1)
plt.plot([m1*x1+b1 for x1 in range(12000)], color='red')
plt.xlim(0,35)
plt.ylim(-10,50)
#-------------------------------------------------------------------------#
testd=pd.read_csv(r'/home/harshal/Downloads/test.csv')
testd['Price']=y_pred
print(testd)
#r2 score
from sklearn.metrics import r2_score
print(r2_score(y_test,y_pred))
# %%
