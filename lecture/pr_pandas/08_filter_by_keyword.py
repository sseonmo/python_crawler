import pandas as pd

df = pd.read_json('./195297.json')
# dfFilter = df[(df['price'] >= 10000) & (df['price'] <= 30000)]

keywords = ['페레로로쉐', '킨더', '트윅스', '엠앤']
totalCount = df['name'].count()
for keyword in keywords:
    dfFiltered = df[df['name'].str.contains(keyword)]
    # print(dfFiltered['name'].head(10))
    # print(dfFiltered[['name', 'price']].sort_values('price', ascending=0).head(20))
    count = dfFiltered['name'].count()
    print(keyword, count, str(round(count / totalCount * 100, 2))+"%")
