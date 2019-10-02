# crewling 하는 코드
import requests
import bs4


# url를 넣어서 bs_obj를 return 하는 funtion

url = "https://finance.naver.com/item/main.nhn?code=005930"
response = requests.get(url)
soup = bs4.BeautifulSoup(response.content, "html.parser")
print(soup)
