import os
class contentSaver:
    __title=''
    __content = ''
    __section = ''
    __type = ''
    def __init__(self,section,title,content,fileType=''):
        self.__section = section
        self.__title = title
        self.__content = content
        if(len(fileType)>0):
            self.__type = '.'+fileType
    
    def save(self):        
        if(not os.path.exists('.\\save\\'+self.__section+'\\')):
            os.makedirs('.\\save\\'+self.__section+'\\')
        with open('.\\save\\'+self.__section+'\\'+self.__title+self.__type,'w',encoding='utf-8') as file1:
            #for i in content: # 按行写
            #        print(i)
            file1.write(self.__content)#写入数据，文件保存在上面指定的目录，按行写时候加\n为了换行更方便阅读

    def currDir(self):
        
        print(os.path.abspath('.'))





sa =contentSaver('点对点','啊','顶顶顶顶顶格外的发生大事','txt')
sa.save()
sa.currDir()