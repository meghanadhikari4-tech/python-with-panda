import pandas as pd
data={
    'place':['thimi','newroad','bhaktapur','gathaghar','lalitpur'],
    'month':['january','februrary','march','april','may'],
    'sales':[125,87,50,78,89]
}
df=pd.DataFrame(data)
df['sales']=pd.to_numeric(df['sales'])
report = df.groupby(['place', 'month'])['sales'].agg(['sum','mean','max','min']).reset_index()
report=report.sort_values(by='place')
#has values only at one month so gives this many nan
pivot=pd.pivot_table(
    df,
    values='sales',
    index='place',
    columns='month',
    aggfunc='sum',
)
print(pivot)

print('the given sales is:\n')
print(report)

