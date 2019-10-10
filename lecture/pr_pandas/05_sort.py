import pandas as pd
pd.set_option('display.max_colwidth', -1)

df = pd.read_json('./195297.json')
print(df.columns)
dfSorted = df.sort_values(['price'], ascending=0)
print(dfSorted.head(5).values)
# print(dfSorted.tail(5).values)
