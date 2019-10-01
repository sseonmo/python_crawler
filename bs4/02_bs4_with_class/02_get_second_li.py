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
    </body>
</html>
"""

soup = bs4.BeautifulSoup(html_str, "html.parser")
# bye 추출
lis = soup.findAll("li")

for li in lis:
    print(li)

