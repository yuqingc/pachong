from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs_obj = BeautifulSoup(html, 'html.parser')
images = bs_obj.findAll('img', {'src': re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images:
    print(image)  # The tag object
    print(image.attrs)  # A dictionary including all attributes of a tag
    print(image['src'])
two_attr_tags = bs_obj.findAll(lambda tag: len(tag.attrs) == 2)
print('The number of two-attr tags is, ', len(two_attr_tags))  # Notice the use of the lambda expression

# Other libs for parsing HTML: lxml HTML parser
