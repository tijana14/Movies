import pandas as pd

df=pd.read_csv("movies.csv", encoding='latin1')
print(df.to_string())