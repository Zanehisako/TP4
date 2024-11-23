import pandas as pd
import matplotlib.pyplot as plt,seaborn as sns

df = pd.read_csv('canada.csv')
year_col = ['RegName'] + [str(year) for year in range(1980,2014)]
df = df.loc[:,year_col]
print(df.head())
df_group:pd.DataFrame = df.groupby('RegName')[year_col].sum()
df_group = df_group.set_index('RegName')
print(df_group.head())

sns.heatmap(df_group)
plt.show()

df_group = df_group.T
df_group.plot(kind='area')
plt.show()
