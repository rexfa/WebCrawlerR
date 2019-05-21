import requests
import json
from lxml import etree
import urllib.request
import re
import os

class docSaver:
    __title=''
    __time =''
    __content = ''
    __section = ''
    __type = 'txt'
    def __init__(self,section,time,title,contentRaw):
        self.__section = section
        self.__title = title
        self.__content = contentRaw
        self.__time = time
        
    def analysis(self):
        self.__content = self.__content.replace('</p>','\n')
        docs = re.findall(r'<ahref=\"(.*)</a>',self.__content) 
        i=0
        docDict={}
        for d in docs:
            docDict[i]= str.split(d,'\">')
            i = i+1
        return docDict

    def save(self,docDict):
        for docUrl in docDict:
            website = urllib.request.urlopen(docUrl)
            self.__type = self.__extension(website)
            if(not os.path.exists('.\\save\\'+self.__section+'\\'+self.__time +'\\')):
                os.makedirs('.\\save\\'+self.__section+'\\'+self.__time +'\\')
            with open('.\\save\\'+self.__section+'\\'+self.__time +'\\'+self.__title+self.__type,'w') as file1:
                #for i in content: # 按行写
                #        print(i)
                file1.write(website.read())
    
    def __extension(self,filename):
        fs = filename.split('.')
        return fs[len(fs)-1]
