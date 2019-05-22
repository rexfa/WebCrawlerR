import homePageReader
import innerPageReader
import contentPageReader
import contentSaver
import imgSaver
import docSaver

homeurl = 'http://10.122.7.5'
home = homePageReader.homePageReader(homeurl) 
mores = home.analysis()
print('more')
print(mores)
print('^^^^^^^^^^^^^^^^^^^^^开始读取内页^^^^^^^^^^^^^^^^^^^^^^^^^^')

def getAllContents(contentUrls,section):
        for c in contentUrls:
                getContent(c,section)

def getContent(contentUrl,section):
        url = homeurl+contentUrl
        con = contentPageReader.contentPageReader(url)        
        title,time,content,contentRaw  = con.analysis()
        docS = docSaver.docSaver(section,time,title,contentRaw)
        imgS = imgSaver.imgSaver(section,time,title,contentRaw)
        print(section)
        print(time)
        print(title)
        print(contentRaw)

        
for ms in mores:
    inner = innerPageReader.innerPageReader(homeurl+ms[1])
    contens = inner.analysis()
    morePages = inner.pageAnalysis()
    print('更多页')
    print(morePages)
    print('链接列表')
    print(contens)
    print('---------------------第1页读完--------------------------------------')
    #getAllContents(contens)
    i=2
    if(morePages != None):
        for ins in morePages:
                inner2 = innerPageReader.innerPageReader(homeurl+ms+ins)
                if(ins.find('.html')<0):
                        inner2 = innerPageReader.innerPageReader(homeurl+ins)
                contens2 = inner2.analysis()
                print(contens2)
                print('---------------------第'+str(i)+'页读完--------------------------------------')
                i = i+1
    

