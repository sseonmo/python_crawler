import pandas as pd

pd.set_option('display.max_colwidth', -1)

df = pd.read_json('./gangnam.json')
df = df.head(200)
# print(df.loc[df['postdate'] == '', :])
df['postdate'] = pd.to_datetime(df['postdate'], format='%Y%m%d', errors='coerce')

# dfUpperJan = df[df['postdate'] >= '2018-01-01']
# print(dfUpperJan.count())


dfJan = df[(df['postdate'] >= '2019-07-01') & (df['postdate'] < '2019-08-01')]
dfFev = df[(df['postdate'] >= '2019-08-01') & (df['postdate'] < '2019-09-01')]
dfMar = df[(df['postdate'] >= '2019-09-01') & (df['postdate'] < '2019-10-01')]
print(dfJan.count())
print(dfFev.count())
print(dfMar.count())
print(dfMar.values)

print(df['postdate'].min())
print(df['postdate'].max())

# 값이 없는 값 삭제
# df.dropna(how='any')
# print(df.loc[df.isnull()['postdate'], :])
# print(df.loc[df['postdate'] == 'NaT', :])



# print(df['postdate'])
# type(df)  # DataFrame
# print(df.head())
# print(df.tail())
# print(df.index)  # "the index" (aka "the labels")
# print(df.columns)  # column names (which is "an index")
# print(df.dtypes)  # data types of each column
# print(df.shape)  # number of rows and columns
# print(df.values)  # underlying numpy array
# print(df.info())  # concise summary (includes memory usage as of pandas 0.15.0
