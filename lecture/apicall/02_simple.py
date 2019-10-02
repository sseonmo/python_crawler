import requests
from urllib.parse import urlparse

client_id = "ABxJswzA_rB4u6I7Q3hR"
client_secret = "NELa3Xj_De"

keyword = "디퓨져"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword  # json 결과
headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}
response = requests.get(urlparse(url).geturl(), headers=headers)

json_obj = response.json()

print(json_obj)