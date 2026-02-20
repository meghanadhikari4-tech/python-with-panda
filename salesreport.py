import pandas as pd
import matplotlib.pyplot as plt  # required for charts
data={
    'place':['thimi']*5+['newroad']*5+['bhaktapur']*5+['gathaghar']*5+['bhaktapur']*5+['lalitpur']*5,
    'month':['january','februrary','march','april','june','may']*5,
    'sales':[125,87,50,78,100,89]*5
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
    fill_value=0,
)
pivot=pivot.sort_values(by='march',ascending=False)
pivot.plot(
    kind='bar',
    fontsize="10",
    colormap="viridis",
    width=0.8
)
plt.title("sales place per month",fontsize="10",fontweight="bold")
plt.xlabel("place",fontsize="10")
plt.tight_layout()
plt.show()
print(pivot)

print('the given sales is:\n')
print(report)





