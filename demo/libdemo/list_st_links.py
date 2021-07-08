import requests
from bs4 import BeautifulSoup

URL = "http://www.srikanthtechnologies.com"
# URL = "https://www.w3schools.com"

resp = requests.get(URL)
if resp.status_code != 200:
    print("Sorry! Couldn't access website {URL}")
    exit(1)

bs = BeautifulSoup(resp.text, 'html.parser')
links = bs.find_all('a')

for link in links:
    if 'href' in link.attrs:
        href = link.attrs['href']
        if href == '#':
            continue

        if not href.startswith("http"):
            if not href.startswith("/"):
                href = URL + "/" + href
            else:
                href = URL + href

        print(href)
