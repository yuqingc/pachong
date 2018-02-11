from bs4 import BeautifulSoup
import re
from urllib.request import urlopen

pages = set()


def get_links(page_url):
    global pages
    html = urlopen("http://en.wikipedia.org" + page_url)
    bs_obj = BeautifulSoup(html, 'html.parser')
    for link in bs_obj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 我们遇到了新页面
                new_page = link.attrs['href']
                print(new_page)
                pages.add(new_page)
                get_links(new_page)  # 递归调用


get_links('')
