import requests
from bs4 import BeautifulSoup


def get_bs_obj():
    url = 'https://finance.naver.com/item/main.nhn?code=005930'
    result = requests.get(url)
    return BeautifulSoup(result.content, 'html.parser')


bs_obj = get_bs_obj()
print(bs_obj)
