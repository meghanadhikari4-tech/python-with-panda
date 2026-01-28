import pandas as pd
df=pd.DataFrame([[1,2,3,4,],[6,7,8,9],[10,11,12,13]], columns=["A","B","C","D"])
print(df)
df.columns
#seeing first rows
df.head(1)
#seeing first two rows
df.head(2)
#bottom two rows
df.tail(2)