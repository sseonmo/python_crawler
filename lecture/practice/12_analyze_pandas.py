import pandas as pd

df = pd.read_json("./gangnam.json")
print(df.count())
dfGrp = df.groupby("bloggername").count()
print(dfGrp)

bloggerNames = df['bloggername']
print(bloggerNames)