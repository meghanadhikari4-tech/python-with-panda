import pandas as pd
data={
    'City': ["bhaktapur",'lalitpur','butwal','palpa','bhaktapur','butwal'],
    'sales': ['120','70','80','95','130','50']
}
df=pd.DataFrame(data)
df['sales']=pd.to_numeric(df['sales'])
result=df.groupby('City')['sales'].sum()
print(result)
mean=df.groupby('City')['sales'].mean()
print("Mean per city:\n",mean)
min=df.groupby('City')['sales'].min()
print("min per city:\n ",min)
max=df.groupby('City')['sales'].max()
print("max per city:\n ",max)
#multiple aggregations
sales=df.groupby("City")['sales'].agg(['sum','mean','min','max'])
print(sales)

