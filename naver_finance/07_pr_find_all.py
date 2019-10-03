from bs4 import BeautifulSoup

html = """
    <html> 
        <table>
            <tr>
                <td class='first'>100</td>
                <td>200</td>
            </tr>
            <tr>
                <td>300</td>
                <td>400</td>
            </tr>
        </table>
    </html>
"""

bs_obj = BeautifulSoup(html, "html.parser")

# 100
print(bs_obj.find("td", {"class": "first"}).text)

# 200
table = bs_obj.find("table")
tr = table.find("tr")
tds = tr.findAll("td") # list[ , ,]
print(tds[1].text)

# 300
trs = table.findAll("tr")
second_tr = trs[1]
td_300 = second_tr.find("td")
print(td_300.text)

#  400
td_400 = second_tr.findAll("td")[1]
print(td_400.text)
