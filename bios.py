import pandas as pd

food=pd.read_csv("./python-for-ai/foods.csv")
food.head()
print(food.head(2))
result=food.loc[food['sold']>35]
print(result)