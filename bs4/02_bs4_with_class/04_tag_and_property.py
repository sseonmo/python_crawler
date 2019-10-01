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

#  tag - element
#  proterty - class, id, title, src, href

# ok no sure
ul_reply = soup.find("ul", {"class": "reply"})
lis = ul_reply.findAll("li")
print(lis)

for li in lis:
    print(li.text)