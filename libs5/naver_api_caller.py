import requests
from urllib.parse import quote

client_id = "ABxJswzA_rB4u6I7Q3hR"
client_secret = "NELa3Xj_De"

def get1000Resutl(keyword):
    list = []
    for num in range(0, 10):
        list += (call(keyword, num * 100 + 1)['items'])
    return list

def call(keyword, start):
    encText = quote(keyword)
    url = 'https://openapi.naver.com/v1/search/blog?query=' + encText + '&display=100&start=' + str(start)
    # print(url)
    headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}
    result = requests.get(url, headers=headers)
    print(result)
    return result.json()
