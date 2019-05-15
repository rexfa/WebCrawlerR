import homePageReader
import innerPageReader

homeurl = 'http://10.122.7.5'
home = homePageReader.homePageReader(homeurl) 
mores = home.analysis()
print('more')
print(mores)
print('^^^^^^^^^^^^^^^^^^^^^开始读取内页^^^^^^^^^^^^^^^^^^^^^^^^^^')

        
for ms in mores:
    inner = innerPageReader.innerPageReader(homeurl+ms)
    contens = inner.analysis()
    morePages = inner.pageAnalysis()
    print('更多页')
    print(morePages)
    print('链接列表')
    print(contens)
    print('---------------------第1页读完--------------------------------------')
    i=2
    for ins in morePages:
        inner2 = innerPageReader.innerPageReader(homeurl+ms+ins)
        contens2 = inner2.analysis()
        print(contens2)
        print('---------------------第'+str(i)+'页读完--------------------------------------')
        i = i+1
    

