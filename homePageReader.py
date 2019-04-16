import requests
import json
from lxml import etree
import urllib.request
import re

class homePageReader:
    __url=''
    def __init__(self,url):
        self.__url = url
    def analysis(self,isLocal):
        if(isLocal):
            html = urllib.request.FileHandler()
            req = urllib.request.Request(self.__url)
            html.file_open(req).read().decode('UTF-8')
            links = re.findall('"((http|ftp)s?://.*?)"', html)
            print(links)
        else:
            website = urllib.request.urlopen(self.__url)
        #read html code
            html = website.read().decode('UTF-8')
        #use re.findall to get all the links
        #links = re.findall('"((http|ftp)s?://.*?)"', html)
            #print(html)
            mores = re.findall('"((http|ftp)s?更多)"',html)
            links = re.findall('"((http|ftp)s?://.*?)"', html)
        #htmlData=requests.get(self.__url).text
        #s=etree.HTML(htmlData)
            #print(links)
            print(mores)


a = homePageReader('file:/D:/VSCode/Python/WebCrawlerR/ExHTML/中国农业科学院作物科学研究所内网.html')
a.analysis(False)
        

