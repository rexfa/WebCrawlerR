import requests
import json
from lxml import etree
# python -m pip install --upgrade pip
# python -m pip install requests
# python -m pip install lxml
# pip install -i requests https://pypi.douban.com/simple
# pip install -i https://pypi.douban.com/simple pandas 
# pip install lxml
# https://zhuanlan.zhihu.com/p/32037625

url = 'https://movie.douban.com/subject/1292052/'
data = requests.get(url).text
s=etree.HTML(data)

film=s.xpath('//*[@id="content"]/h1/span[1]/text()')
titlePic = s.xpath('//*[@id="mainpic"]/a/img')
srcPic = titlePic[0].attrib
#jd = json.dump(srcPIC)
print(film)
print(titlePic)
print(srcPic)
print(srcPic['src'])