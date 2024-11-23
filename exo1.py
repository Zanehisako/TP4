import pandas as pd
import matplotlib.pyplot as plt,seaborn as sns

df = pd.read_csv('players.csv')
#Question 1
df.current_club_id =df.current_club_id.astype('category')
print(df.current_club_id.describe())

#Question 2
df.contract_expiration_date = pd.to_datetime(df.contract_expiration_date)
df_contrat:pd.DataFrame = df.loc[df.contract_expiration_date.dt.year > 2024] 
print(df_contrat.head())
df_contrat['year_remaining'] = df_contrat['contract_expiration_date'].dt.year - 2024
print(df_contrat['year_remaining'].head())

#Question 3
df.date_of_birth = pd.to_datetime(df.date_of_birth)
df_contrat['age'] = 2024 - df.date_of_birth.dt.year 
print(df_contrat['age'].head)
#qcut divise a par a raport un percenage[0,1] cut divise par a raport des bins
df_contrat['age_bracket'] = pd.cut(df_contrat.age,bins=[12,17,20,24,28,35,60])
print(df_contrat['age_bracket'].tail())
print(df_contrat['age_bracket'].value_counts())
print('la valuer maximal pour chaque tranch est:')
print(df_contrat.groupby('age_bracket')['market_value_in_eur'].max())

df_contrat['market_value_bracket'] = pd.qcut(df_contrat.market_value_in_eur,q=6)
print(df_contrat['market_value_bracket'].tail())
df_contrat= df_contrat.sort_values(by=['market_value_bracket'],ascending=False)
print(df_contrat.head())

#Part Two Visualisation des données
#Question 1
"""
market_value= df_contrat['market_value_in_eur'].dropna()
sns.lineplot(x=df_contrat.year_remaining,y=market_value)
plt.show()
"""
#Question 2
"""
sns.lineplot(data=df_contrat.set_index('age')[['market_value_in_eur','highest_market_value_in_eur']],errorbar=None)
plt.show()
"""
#Multiplle plots
fg =sns.FacetGrid(df_contrat,col="age_bracket",col_wrap=3)
fg.map(sns.lineplot,"age","market_value_in_eur")
plt.show()


