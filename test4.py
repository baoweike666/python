# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup 
import sys
reload(sys)
sys.setdefaultencoding('utf8')
res = urllib.urlopen("http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=book")
soup = BeautifulSoup(res,"html.parser")
book_div = soup.find(attrs={"id":"book"})
book_a = book_div.findAll(attrs={"class":"title"})
for book in book_a:
    #print book.string
    with open("/home/omega/data4.txt",'a+') as fd:
     fd.write(book.string+"\n")