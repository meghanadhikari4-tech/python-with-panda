import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.model_selection import train_test_split
df={
    "hours":[1,2,3,4,5],
    "score":[55,60,65,70,75]
}
result=pd.DataFrame(df)
Standard_scaler=StandardScaler()
Standard_scaled=Standard_scaler.fit_transform(result)
print("standard_scaler output:")
print(pd.DataFrame (Standard_scaled,columns=["hours","score"]))
minmax_scaler=MinMaxScaler()
minmax_scaled=minmax_scaler.fit_transform(result)
print("/n minmax_scaler output:")
print(pd.DataFrame(minmax_scaled,columns=["hours","score"]))
X=result[["hours"]]
y=result[["score"]]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print("training data")
print(X_train)
print("testing data")
print(X_test)
print("training data")
print(y_train)
print("testing data")
print(y_test)
