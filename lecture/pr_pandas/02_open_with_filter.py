import pandas as pd
pd.set_option('display.max_colwidth', -1)


df = pd.read_json('./gangnam.json')

# print(df.count())
# filter
# dfFiltered = df[df['bloggername'] == '소래비로에 오래된새댁']
dfFiltered = df[df['bloggername'] == '올리비아케이 공식블로그']
print(dfFiltered[['bloggername', 'link']])
