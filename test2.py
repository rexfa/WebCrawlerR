import homePageReader
import innerPageReader
# http://10.122.7.5/
a = homePageReader.homePageReader('file:ExHTML/中国农业科学院作物科学研究所内网.html') 
mores = a.analysis()
print(mores)


inner = innerPageReader.innerPageReader('file:ExHTML/科研信息_中国农业科学院作物科学研究所内网.html') 
#a.analysis(False)
inner.pageAnalysis()