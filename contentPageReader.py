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
        title = re.findall(r'<meta name=\"description\" content=\"(.*)\">',html)[0]
        # xpath = /html/body/div[3]/div[1]/div[2]/div[4]
        # /html/body/div[3]/div[1]/div[2]/div[4]/table
        #替换掉空格换行回车后注意式子里没有这些字符了
        htmlClear = html.replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '')
        contentRaw = re.findall(r'<divclass=\"content\"><tablewidth=\"100%\"><tbody><tr><td>(.*)</td></tr></tbody></table></div>',htmlClear)[0]
        content=''
        try:
            content = re.findall(r'<divid=\"contentMidPicAD"style="float:right;clear:both;top:0;vertical-align:top;"></div><pstyle=\"text-indent:2em;\">(.*)</p><pstyle=\"text-align:right;\">',contentRaw)[0]    
        except:
            content=''
        time = re.findall(r'时间:</small>(.*)<small>来源',html)[0]
        #timeR0 = re.findall(r'<br>(.*)</p>',timeRaw)
        #time = str.split(timeR0[0],'</p>')[0]
        #content = htmlClear[htmlClear.find("<div class=\"content\">")+1:htmlClear.rfind("</td></tr></tbody></table></div>")]
        # print(htmlClear)
        #content = re.findall(r'<div class=\"content\"><table width=\"100%\">(.*)</tbody></table></div>',html)
        # htmlTree = etree.HTML(html)
        # content = htmlTree.xpath('/html/body/div[3]/div[1]/div[2]/div[4]')
        # print(title,content,time) # 显示结果
        # print(time)
        #print(htmlClear.find("<div class=\"content\">"))
        
        content = self.cleanHTML(content)
        return title,time,content,contentRaw

    def getinnerhtml(self,data):
        i=0
        leftT = []
        rightT= []
        while True:
            try:
                i = data.index('<',i+1)
                leftT.append(i)
            except:
                break
        i=0
        while True:
            try:
                i = data.index('>',i+1)
                rightT.append(i)
            except:
                break        
        return leftT,rightT
    def cleanHTML(self,content):
        leftT,rightT = self.getinnerhtml(content)
        if(len(leftT)!=len(rightT)):
            raise Exception('The number of symbols(<,>) does not match')
        if(len(leftT)==0):
            return content
        l = len(leftT)
        for i in range(l,0,-1): #逆循环
            content = content[:leftT[i-1]] + content[rightT[i-1]+1:]
        return content




a = contentPageReader('file:ExHTML/作科所参保人员领取待遇申请表及职工离所离岗手续清单_中国农业科学院作物科学研究所内网.html')
tl,t,c,craw = a.analysis()
print(tl)
print(c)
print(t)
print(craw)
craw = craw.replace('</p>','\n')
docs = re.findall(r'<ahref=\"(.*)</a>',craw)
print(docs)
# print(a.cleanHTML(c))
# imgs = re.findall(r'src=\"(.*)\"style=',c)
# print(imgs)
# str1="<a>OK<b>[推荐]</b></a>"
# print(a.getinnerhtml(str1))