import requests
import json
from lxml import etree

class crawlerClass:
    __url=''
    def __init__(self,url):
        self.__url = url
    def crawlerHtml(self,xpathTitle,xpathContent):
        htmlData=requests.get(self.__url).text
        s=etree.HTML(htmlData)
        docTitle = s.xpath(xpathTitle)
        docContent = s.xpath(xpathContent)
        return docTitle,docContent