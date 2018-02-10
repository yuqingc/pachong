from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError


def get_title(url_arg: str):
    """This function is used to get the title in an h1 tag of a page"""

    try:
        html = urlopen(url_arg)
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


if __name__ == '__main__':
    test_url = 'http://www.pythonscraping.com/pages/page1.html'
    title = get_title(test_url)
    if title is None:
        print('Title is None')
    else:
        print('Final title is, ', title)
