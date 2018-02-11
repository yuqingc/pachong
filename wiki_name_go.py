from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import datetime
import random

random.seed(datetime.datetime.now())


def get_links(article_url):
    html = urlopen('http://en.wikipedia.org' + article_url)
    soup = BeautifulSoup(html, 'html.parser')
    return soup.findAll('a', {'href': re.compile('^(/wiki/)((?!:).)*$')})


links = get_links('/wiki/Kevin_Bacon')
# 随机选择一个url进行爬虫 直到手动停止或者爬不到链接为止
while len(links) > 0:
    new_article = links[random.randint(0, len(links) - 1)].attrs['href']
    print(new_article)
    links = get_links(new_article)
