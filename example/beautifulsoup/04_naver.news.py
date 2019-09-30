from urllib.request import urlopen
import bs4

url = "https://news.naver.com"
html = urlopen(url)
bs_obj = bs4.BeautifulSoup(html, "html.parser")
lis = bs_obj.find("ul", {"class": "hdline_article_list"}).findAll("li")

for li in lis:
    print("오늘의 헤드라인 : ", li.find("a").text.strip())
# print(bs_obj)

# 배열로 감사기
lis_ = [li.find("a").text for li in lis]
print(lis_)