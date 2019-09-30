import urllib.request
import bs4

html = urllib.request.urlopen("https://www.naver.com")
bsObj = bs4.BeautifulSoup(html, "html.parser")

# print(html.read())
# print(bsObj)
top_right = bsObj.find("div", {"class": "area_links"})
# print(top_right)
first_a = top_right.find("a")
print(first_a.text)
