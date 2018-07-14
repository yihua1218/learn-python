import os
import urllib.request
import urllib.parse

from urllib.request import pathname2url
from bs4 import BeautifulSoup


url = urllib.parse.urljoin('file:', pathname2url(os.path.abspath('ratingValue.html')))
f = urllib.request.urlopen(url)
html_doc = f.read().decode('utf-8')
# print(html_doc)

soup = BeautifulSoup(html_doc, 'html.parser')
items = soup.find_all('span', { "itemprop": "ratingValue" })
for item in items:
  value = item.get_text()
  print(value)