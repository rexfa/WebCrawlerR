import requests
import json
from lxml import etree
import urllib.request
import re

class homePageReader:
    __url=''
    def __init__(self,url):
        self.__url = url
    def analysis(self):
        #if(isLocal):
        #    html = urllib.request.FileHandler()
        #    req = urllib.request.Request(self.__url)
        #    html.file_open(req).read().decode('UTF-8')
        #    links = re.findall('"((http|ftp)s?://.*?)"', html)
        #    print(links)
        #else:
        website = urllib.request.urlopen(self.__url)
        #read html code
        html = website.read().decode('UTF-8')
        #use re.findall to get all the links
        #links = re.findall('"((http|ftp)s?://.*?)"', html)
            #print(html)
            # 正则表达式分析首页链接
        mores = re.findall(r'more\"><a href=\"(.*)\">更多',html)
        return mores

#没有host的 就是一个/ file:/
#相对地址冒号后面就不要/了
a = homePageReader('file:ExHTML/中国农业科学院作物科学研究所内网.html') 
mores = a.analysis()
print(mores)
        

