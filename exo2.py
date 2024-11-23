import matplotlib.pyplot as plt,seaborn as sns,pandas as pd

df = pd.read_csv('game_events.csv',nrows=100000,low_memory=False)
plt.pie(df['type'].value_counts(),labels=df['type'].unique(),autopct='%1.1f%%',explode=[0.05,0,0,0,0,0,0,0],startangle=45,pctdistance=1.2,labeldistance=0.6)
plt.show()

plt.pie(df['type'].value_counts(),labels=df['type'].unique(),autopct='%1.1f%%',explode=[0.05,0,0,0,0,0,0,0],startangle=45,pctdistance=1.2,labeldistance=0.6,wedgeprops={"width":0.2,"edgecolor":'w'})
plt.show()
