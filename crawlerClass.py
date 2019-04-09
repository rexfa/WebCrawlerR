import requests
import json
from lxml import etree

class crawlerClass:
    __url=''
    def __init__(self,url):
        self.__url = url
    def crawlerAndSave(self):
        