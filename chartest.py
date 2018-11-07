import chardet
# str1="我们"
# print(str1)
# print(type(str1))
# str_utf8 = str1.encode('utf-8')
# print(str_utf8)
# print(type(str_utf8))
# new_str = str_utf8.decode('utf-8')
# print(new_str)
# print(type(new_str))
# print(chardet.detect(str_utf8))

import requests
from bs4 import BeautifulSoup

url = 'http://w3school.com.cn/'
r = requests.get(url)
r.encoding = 'gb2312'
soup = BeautifulSoup(r.text,"lxml")
xx = soup.find('div',class_='idea').h2.text
# print(chardet.detect(xx))
print(xx)