from libs.stringGetter import getPageString
from libs.getProductParser import getProducts
from bs4 import BeautifulSoup

categoryProducts = []

for page in range(1, 100):
    url = 'https://www.coupang.com/np/categories/186764?page={}'.format(page)
    print(url)
    pageString = getPageString(url)
    product = getProducts(pageString)
    if product == None:
        break

    categoryProducts += product

print(len(categoryProducts))
# print(categoryProducts)
for product in categoryProducts:
    print(product)
