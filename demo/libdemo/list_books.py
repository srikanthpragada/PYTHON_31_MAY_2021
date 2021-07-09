# Read books info from books.xml and display title and price
from bs4 import BeautifulSoup

f = open("books.xml", "rt")
bs = BeautifulSoup(f.read(), 'xml')
f.close()

print('Subject : ', bs.subject.attrs['title'])
books = bs.subject.find_all("book")

for book in books:
    title = book.find("title").text
    price = book.find("price").text
    print(f"{title:30} {int(price):5}")
