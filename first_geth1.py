from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError


def get_title(urlarg: str):
    """This function is used to get the title in an h1 tag of a page"""

    try:
        html = urlopen(urlarg)

    except HTTPError as e:
        print('There is an HTTPError', e)
        return None

    try:
        bs_obj = BeautifulSoup(html.read(), 'html.parser')
        res_title = bs_obj.body.h1
    except AttributeError as e:
        print('Cannot read attribute, ', e)
        return None
    return res_title


title = get_title('http://www.pythonscraping.com/pages/page1.html')
print('Final title is, ', title)