import pandas as pd

df = pd.read_csv('kijijiauto.csv')
df = df.dropna(subset=['year'], inplace=True)
print(df)