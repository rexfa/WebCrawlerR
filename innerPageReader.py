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
        #mores = re.findall(r'] <a href=\"(.*)\" class=\"title',html)
        titleRaw = re.findall(r'\[<b>(.*)\" class=\"title',html)
        classTitleDice = {}
        i = 0
        for t in titleRaw:
            ts = re.findall(r'\">(.*)</a></b>]',t)
            cs = re.findall(r'</a></b>] <a href=\"(.*)',t)
            vaule=[ts[0],cs[0]]
            classTitleDice[i]=vaule
            i=i+1
        #print(titleRaw)
        print(classTitleDice)
        return classTitleDice
    def pageAnalysis(self):
        website = urllib.request.urlopen(self.__url)
        html = website.read().decode('UTF-8')
        secondPage = re.findall(r'<li><a href=\"(.*)\">2</a></li>',html)
        nextPage = re.findall(r'<li><a href=\"(.*)\">下一页</a></li>',html)
        lastPage = re.findall(r'<li><a href=\"(.*)\">末页</a></li>',html)
        morePages = []
        if(len(secondPage)>0):
             # 计算出有多少分页 页面
             numStr = re.findall(r'list_(.*).html',lastPage[0])[0]
             start0 = lastPage[0].split('_')[0]
             start1= lastPage[0].split('_')[1]
             lastNumString = numStr.split('_')[1]
             lastNum =int(lastNumString)
             for i in range(1,lastNum):
                # 循环组合出所有分页页面
                # 注意+1
                p = start0+"_"+start1+"_"+str(i+1)+".html"
                morePages.append(p)
        print(secondPage,nextPage,lastPage)
        print(morePages)
        return morePages

#相对地址冒号后面就不要/了
a = innerPageReader('file:ExHTML/科研信息_中国农业科学院作物科学研究所内网.html') 
#a.analysis(False)
a.pageAnalysis()