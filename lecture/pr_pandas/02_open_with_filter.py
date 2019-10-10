import pandas as pd

pd.set_option('display.max_colwidth', -1)

df = pd.read_json('./gangnam.json')

# print(df.count())
# filter
# dfFiltered = df[df['bloggername'] == '소래비로에 오래된새댁']
dfFiltered = df[df['bloggername'] == '올리비아케이 공식블로그']
print(dfFiltered[['bloggername', 'link']])
# print(dfFiltered.values)
#
# type(df)  # DataFrame
# print(df.head())
# print(df.tail())
# print(df.index)  # "the index" (aka "the labels")
# print(df.columns)  # column names (which is "an index")
# print(df.dtypes)  # data types of each column
# print(df.shape)  # number of rows and columns
# print(df.values)  # underlying numpy array
# print(df.info())  # concise summary (includes memory usage as of pandas 0.15.0
