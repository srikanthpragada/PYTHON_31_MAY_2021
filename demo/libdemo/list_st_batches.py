import requests
from bs4 import BeautifulSoup

URL = "http://www.srikanthtechnologies.com"

resp = requests.get(URL)
if resp.status_code != 200:
    print("Sorry! Couldn't access website {URL}")
    exit(1)

bs = BeautifulSoup(resp.text, 'html.parser')
table = bs.find(id="ctl00_ContentPlaceHolder1_GridView2")
if table is None:
    print("Sorry! Could not get details!")
    exit(1)

rows = table.find_all("tr")[1:]

for row in rows:
    cols = row.find_all("td")
    print(f"{cols[0].text:30} {cols[1].text:10}  {cols[2].text:10}")
