from libs.naver_shopping.crawler import crawl
from libs.naver_shopping.parser import parse
import json

pageString = crawl('숨셔바요')
products = parse(pageString)
print(len(products))
[print(product) for product in products]

# json 저장
file = open('./products.json', 'w+')
file.write(json.dumps(products))
