import requests
from bs4 import BeautifulSoup

domain = 'https://www.ncbi.nlm.nih.gov'
url = '{}/pubmed/?term=AML'.format(domain)

result = requests.get(url)
bsObj = BeautifulSoup(result.content, 'html.parser')
content = bsObj.find('div', {'class': 'content'})
rprts = content.findAll('div',{'class': 'rprt'})

for item in rprts:
    find_a = item.find('a')
    link = '{}{}'.format(domain, find_a.get('href'))
    print(link, find_a.text)

    linkResult = requests.get(link)
    soup = BeautifulSoup(linkResult.content, 'html.parser')
    subRprt = soup.find("div", {'class': 'rprt_all'})
    print(subRprt.find('h1').text)


