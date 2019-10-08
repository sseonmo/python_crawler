from bs4 import BeautifulSoup

def getProduct(li):
    img = li.find('dt', {'class': 'image'}).find('img')
    price = li.find('strong', {'class': 'price-value'})
    return {'name': img['alt'], 'price': price.text}

def getProducts(pageStr):
    bsObj = BeautifulSoup(pageStr, 'html.parser')
    ul = bsObj.find('ul', {'id': 'productList'})
    if ul == None:
        return None
    lis = ul.findAll('li')
    return list(map(getProduct, lis))
