from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()


def get_links(url_link):
    global pages
    html = urlopen("http://en.wikipedia.org" + url_link)
    bs_obj = BeautifulSoup(html, 'html.parser')
    try:
        print(bs_obj.h1.get_text())
        print(bs_obj.find(id='mw-content-text').findAll('p')[0])
        print(bs_obj.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError as e:
        print('Some attributes cannot be found but no worries')

    for link in bs_obj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs and link.attrs['href'] not in pages:
            new_page = link.attrs['href']
            print('-----------------\n' + new_page)
            pages.add(new_page)
            get_links(new_page)


if __name__ == '__main__':
    print('Starting main...')
    get_links('')