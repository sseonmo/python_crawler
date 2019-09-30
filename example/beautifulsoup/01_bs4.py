import bs4

# pip install bs4 - install script
html_str = "<html><div></div></html>"
bsObj = bs4.BeautifulSoup(html_str, "html.parser")

print(type(bsObj))
print(bsObj)
print(bsObj.find("div"))
