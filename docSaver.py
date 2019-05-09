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
    __type = ''
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
