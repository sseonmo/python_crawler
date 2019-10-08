from libs.stringGetter import getPageString
from libs.getProductParser import  getProducts
from bs4 import BeautifulSoup

url = 'https://www.coupang.com/np/categories/186764?page=2'
pageString = getPageString(url)
for product in getProducts(pageString):
    print(product)