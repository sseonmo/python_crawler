import requests
from libs.naver_shopping.parser import parse
import json

def crawl(pageNumger):
    url = 'https://search.shopping.naver.com/search/all.nhn?query=텀플러&cat_id=&pagingIndex={}&frm=NVSHATC'.format(
        pageNumger)
    data = requests.get(url)
    print(data, url)
    return data.content

# pageString = crawl(4)
# products = parse(pageString)
# print(products)
# print(len(products))

totalProducts = []

# for pageNo in range(0, 10+1):
#     pageString = crawl(pageNo)
#     product = parse(pageString)
#     totalProducts += product

for pageString in map(crawl, range(1, 11)):
    totalProducts += parse(pageString)

# pageString = list())
# totalProducts += list(map(parse, pageString))
print(len(totalProducts))

file = open('./tumbler.json', 'w+')
file.write(json.dumps(totalProducts))


