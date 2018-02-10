from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError

url = 'http://www.pythonscraping.com/pages/warandpeace.html'
try:
    html = urlopen(url)
except HTTPError as e:
    print('There is an HTTPError', e)
else:
    bs_obj = BeautifulSoup(html, 'html.parser')
    name_list = bs_obj.findAll('span', {'class': 'green'})
    for name in name_list:
        print(name.getText())