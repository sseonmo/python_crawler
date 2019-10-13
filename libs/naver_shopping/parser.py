from bs4 import BeautifulSoup

def getProductInfo(li):
    alt = li.find('img', {'class': '_productLazyImg'})['alt']
    _price_reload = li.find('span', {'class': '_price_reload'})
    img = li.find('a', {'class': 'img'})

    # 예외처리
    try:
        price = _price_reload.text
    except AttributeError:
        price = '0'

    try:
        link = img['href']
    except AttributeError:
        link = ''

    return {'name': alt, 'price': price.replace(',', ''), 'link': link}

def parse(pageString):
    bsObj = BeautifulSoup(pageString, 'html.parser')
    ul = bsObj.find('ul', {'class': 'goods_list'})
    lis = ul.findAll('li', {'class': '_itemSection'})

    # print(len(lis))
    # print(lis[0])
    product = list(map(getProductInfo, lis))
    return product
