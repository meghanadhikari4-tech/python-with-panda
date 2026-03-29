import pandas as pd
data=pd.read_csv("disease.csv")
print(data.head())
from sklearn.model_selection import train_test_split
X=data.drop("Outcome",axis=1)
y=data["Outcome"]
from sklearn.linear_model import LogisticRegression
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
model=LogisticRegression()
model.fit(X_train,y_train)
from sklearn.metrics import accuracy_score
y_pred=model.predict(X_test)
print("accouracy:",accuracy_score(y_test,y_pred))
sample=[99,80,67,56,45,78,89,76,57,89]
print(sample)