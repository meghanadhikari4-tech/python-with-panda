from sklearn.metrics import accuracy_score,precision_score, recall_score,f1_score
y_true=[0,1,1,0,1,0]
y_pred=[1,1,0,0,1,1]
print("Accuracy:",accuracy_score(y_true,y_pred))
print("precision_score:",accuracy_score(y_true,y_pred))
print("recall_score:",accuracy_score(y_true,y_pred))
print("f1_score:",accuracy_score(y_true,y_pred))

from sklearn.metrics import confusion_matrix
y_true=[0,1,1,0,1,0]
y_pred=[1,1,0,0,1,1]
c=confusion_matrix(y_true,y_pred)
print(c)


