import requests
from bs4 import BeautifulSoup

domain = 'http://www.netd.ac.za/'
# url = '{}?action=browse&category=Affiliation&order=asc'.format(domain)
pagingUrl = '{}portal/?action=browse&category=Affiliation&maxresults=10&start={}&order=asc'

ols = []
for i in range(0, 3):
    url_format = pagingUrl.format(domain, i * 10 + 1)
    print(url_format)
    result = requests.get(url_format)
    if result.status_code != 200:
        break
    ols.append(BeautifulSoup(result.content, 'html.parser').find('ol'))

print(len(ols))

for ol in ols:
    for li in ol.findAll('li'):
        print('{}{}'.format(domain, li.find('a').get('href')))

#
# result = requests.get(url)
# bsObj = BeautifulSoup(result.content, 'html.parser')
# ol = bsObj.find('ol')
# lis = ol.findAll('li')
# for li in lis:
#     print('{}?{}'.format(domain, li.find('a').get('href')))
#
# # action=view&identifier=oai%3Aunion.ndltd.org%3Acput%2Foai%3Alocalhost%3A20.500.11838%2F727
