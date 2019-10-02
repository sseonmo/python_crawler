# crewling 하는 코드
import requests
import bs4


# url를 넣어서 bs_obj를 return 하는 funtion
def get_bs_obj(url):
    response = requests.get(url)
    if response.status_code == 200:
        return bs4.BeautifulSoup(response.content, "html.parser")

    return


url = "https://finance.naver.com/item/main.nhn?code=005930"
print(get_bs_obj(url))
