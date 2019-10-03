import requests
from bs4 import BeautifulSoup


def get_bs_obj(company_code):
    url = 'https://finance.naver.com/item/main.nhn?code={}'.format(company_code)
    result = requests.get(url)
    return BeautifulSoup(result.content, 'html.parser')


# bs_obj 받아서 price를 reutrn
def get_price(company_code):
    bs_obj = get_bs_obj(company_code)
    no_today = bs_obj.find("p", {"class": "no_today"})
    blind_now = no_today.find("span", {"class": "blind"})
    return blind_now.text


company_codes = ['005930', '000660', '005680']
for company in company_codes:
    print(get_price(company)) 
