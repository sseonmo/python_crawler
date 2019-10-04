import requests
from bs4 import BeautifulSoup

def get_bs_obj(company_code):
    url = 'https://finance.naver.com/item/main.nhn?code={}'.format(company_code)
    result = requests.get(url)
    return BeautifulSoup(result.content, 'html.parser')

# bs_obj 받아서 price를 reutrn
def get_candel_chart_data(company_code):
    bs_obj = get_bs_obj(company_code)
    # print(bs_obj)
    trs = bs_obj("table", {"class": "no_info"})[0].findAll("tr")
    tds = bs_obj.findAll("td", {"class": "first"})

    #  close 종가(전일)
    close = tds[0].find("span", {"class", "blind"}).text

    # high(고가)
    second_td_1 = trs[0].findAll("td")[1]
    high = second_td_1.find("span", {"class", "blind"}).text

    # open(시가)
    open = tds[1].find("span", {"class", "blind"}).text

    # row(저가)
    second_td_2 = trs[1].findAll("td")[1]
    low = second_td_2.find("span", {"class", "blind"}).text

    return {"close": close, "high": high, "open": open, "low": low}

# sk hynix : 000660, naver : 035420
# 1
# print(get_candel_chart_data('000660'))
# print(get_candel_chart_data('035420'))
# 2
company_codes = ['000660', '035420', '034220']
# print(list(map(get_candel_chart_data, company_codes)))

# 3
for price in map(get_candel_chart_data, company_codes):
    print(price)
