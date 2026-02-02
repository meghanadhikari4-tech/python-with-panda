import numpy as np
import pandas as pd
dict1={
    "name":['megghan','roshan','sita','gita'],
    "marks":[99, 26,24,67]
}

df=pd.DataFrame(dict1)
df.to_csv("meghan.csv")#to print in excel
newdf=pd.DataFrame(np.random.rand(234,5),index=np.arange(234))
type(newdf)
newdf.to_numpy()
print(newdf)
print(df.describe())
print(df)

 