import bs4

html_str = """
<html>
    <body>
        <ul class="greet">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class="reply">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
        <ul>
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>
"""

soup = bs4.BeautifulSoup(html_str, "html.parser")
# bye 추출
lis = soup.findAll("li")
# print(type(lis))
# print(lis[1].text)

# 1이상 2이하
for li in lis[1:2]:
    print(li.text)
