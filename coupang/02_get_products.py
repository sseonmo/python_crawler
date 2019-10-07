from libs.stringGetter import getPageString
from bs4 import BeautifulSoup

def getProduct(pageStr):
    bsObj = BeautifulSoup(pageStr, 'html.parser')
    ul = bsObj.find('ul', {'id': 'productList'})
    lis = ul.findAll('li')
    print(len(lis))
    return bsObj

url = 'https://www.coupang.com/np/categories/186764?page=2'
pageString = getPageString(url)
getProduct(pageString)
