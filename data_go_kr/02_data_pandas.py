import pandas as pd
import json
import os

with open('./sise.json', 'r') as f:
    json_data = json.load(f)

# 엑셀 헤더정보
df = pd.DataFrame(columns=['No', '월', '일', '단지', ' 거래금액', '층', '전용면적'])

items_ = json_data['response']['body']['items']['item']

i = 0
for item in items_:
    df.loc[i] = [i+1, item['월'], item['일'], item['단지'], item['거래금액'], item['층'],  item['전용면적']]
    i = i+ 1

# df.to_csv(os.path.join('./', '시세.csv'), encoding='UTF-8', index=False)
df.to_csv('./시세.csv', encoding='UTF-8', index=False)
