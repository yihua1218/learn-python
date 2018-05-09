import urllib.request
import urllib.parse


url = 'https://www.water.gov.tw/opendata/supp7.csv'
f = urllib.request.urlopen(url)
print(f.read().decode('utf-8'))