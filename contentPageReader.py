import requests
import json
from lxml import etree
import urllib.request
import re

class contentPageReader:
    __url=''
    def __init__(self,url):
        self.__url = url
    def analysis(self):
        website = urllib.request.urlopen(self.__url)
        #read html code
        html = website.read().decode('UTF-8')
        title = re.findall(r'<meta name=\"description\" content=\"(.*)\">',html)
        # xpath = /html/body/div[3]/div[1]/div[2]/div[4]
        # /html/body/div[3]/div[1]/div[2]/div[4]/table
        #替换掉空格换行回车后注意式子里没有这些字符了
        htmlClear = html.replace(' ', '').replace('\n', '').replace('\r', '')
        content = re.findall(r'<divclass=\"content\"><tablewidth=\"100%\"><tbody><tr><td>(.*)</td></tr></tbody></table></div>',htmlClear)
        #content = htmlClear[htmlClear.find("<div class=\"content\">")+1:htmlClear.rfind("</td></tr></tbody></table></div>")]
        # print(htmlClear)
        #content = re.findall(r'<div class=\"content\"><table width=\"100%\">(.*)</tbody></table></div>',html)
        # htmlTree = etree.HTML(html)
        # content = htmlTree.xpath('/html/body/div[3]/div[1]/div[2]/div[4]')
        print(title,content)
        #print(htmlClear.find("<div class=\"content\">"))
        return

    def getinnerhtml(self,data):
        return data[data.find(">")+1:data.rfind("</")]



a = contentPageReader('file:ExHTML/所领导慰问春节期间安全值班人员_中国农业科学院作物科学研究所内网.html')
a.analysis()
# str1="<a>OK<b>[推荐]</b></a>"
# print(a.getinnerhtml(str1))