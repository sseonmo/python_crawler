import requests

def crawl(keyword):
    # 숨셔바요 - %EC%88%A8%EC%85%94%EB%B0%94%EC%9A%94
    url = 'https://search.shopping.naver.com/search/all.nhn?query=숨셔바요&cat_id=&frm=NVSHATC'
    data = requests.get(url)
    print(data.status_code, url)
    return data.content
