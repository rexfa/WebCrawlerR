import requests
import json
import lxml
# pip install -i requests https://pypi.douban.com/simple
# pip install -i https://pypi.douban.com/simple pandas 
# pip install lxml
# https://zhuanlan.zhihu.com/p/32037625

url = 'https://movie.douban.com/subject/1292052/'
data = requests.get(url).text
s=etree.HTML(data)

film=s.xpath('//*[@id="content"]/h1/span[1]/text()')
print(film)