import requests
import json
from lxml import etree
import urllib.request
import re
import os

class imgSaver:
    __title=''
    __content = ''
    __section = ''
    __type = ''
    def __init__(self,section,title,content):
        self.__section = section
        self.__title = title
        self.__content = content
    def analysisAndSave(self):
        imgs = re.findall(r'src=\"(.*)\"style=',self.__content)
        self.__save(imgs)

    def __save(self,imgs):
        for imgUrl in imgs:
            website = urllib.request.urlopen(imgUrl)
            #read html code
            img = website.read()
        if(not os.path.exists('.\\save\\'+self.__section+'\\')):
            os.makedirs('.\\save\\'+self.__section+'\\')
        with open('.\\save\\'+self.__section+'\\'+self.__title+self.__type,'w',encoding='utf-8') as file1:
            #for i in content: # 按行写
            #        print(i)
            file1.write(self.__content)