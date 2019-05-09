import contentPageReader
import imgSaver
import docSaver

a = contentPageReader.contentPageReader('file:ExHTML/作科所参保人员领取待遇申请表及职工离所离岗手续清单_中国农业科学院作物科学研究所内网.html')
#a = contentPageReader.contentPageReader('file:ExHTML/关于印发《中国农业科学院作物科学研究所%20技术服务全成本核算管理办法》的通知_中国农业科学院作物科学研究所内网.html')
#a = contentPageReader.contentPageReader('file:ExHTML/所领导慰问春节期间安全值班人员_中国农业科学院作物科学研究所内网.html')
tl,t,c,craw = a.analysis()
print(tl)
print(c)
print(t)
print(craw)

imgA = imgSaver.imgSaver(tl,t,c,craw)
imgs = imgA.analysis()
print(imgs)

docA = docSaver.docSaver(tl,t,c,craw)
docs = docA.analysis()

print(docs)
