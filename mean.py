import pandas as pd
clg={
    "Name":['sita','gita','rita','nita'],
    "Marks":['19','28','39','40']
}
df=pd.DataFrame(clg)
df["Marks"]=df['Marks'].astype(int)
average=df["Marks"].mean()
print("Average marks:",average)