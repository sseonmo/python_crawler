import requests

def getPageString(pUrl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    data = requests.get(pUrl, headers=headers)
    if data.status_code != 200:
        return None
    return data.content
