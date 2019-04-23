import requests
import json
from lxml import etree
import urllib.request
import re

class innerPageReader:
    __url=''
    def __init__(self,url):
        self.__url = url
    def analysis(self,isLocal):
        website = urllib.request.urlopen(self.__url)
        #read html code
        html = website.read().decode('UTF-8')
        mores = re.findall(r'] <a href=\"(.*)\" class=\"title',html)
        print(mores)
        return mores


a = innerPageReader('file:/D:/VSCode/works/Python/src/WebCrawlerR/ExHTML/科研信息_中国农业科学院作物科学研究所内网.html')
a.analysis(False)