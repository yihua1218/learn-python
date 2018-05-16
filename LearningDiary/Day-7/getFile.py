import urllib.request
import urllib.parse

from bs4 import BeautifulSoup


url = 'http://search.books.com.tw/search/query/key/%E8%82%A1%E5%B8%82/cat/all'
f = urllib.request.urlopen(url)
html_doc = f.read().decode('utf-8')
# print(html_doc)

soup = BeautifulSoup(html_doc, 'html.parser')
items = soup.find_all('li', 'item')
for item in items:
  title = item.find('a')['title']
  print(title)