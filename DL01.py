import string #获取空白字符串whitespace方法

f=open('happiness_seg.txt',encoding='utf-8')#用utf-8的格式打开文本
r=f.readlines()

t=r[:10]#取一段文本进行调试
def cleanpile(t):
    res=[]
    for i in t:
        word=i.split(' ')#以空格为分隔符进行分割，生成分割后的列表
        for item in word:
            items=item.strip('\n')#去掉列表中每一项头尾的换行符
            res.append(items)
    return res

def shaixuan(t):#筛选出列表中长度=2的项，
    res=[]
    for i in t:
        if len(i)==2:
            res.append(i)
    return res

def jishu(t):#对列表中所有项进行计数
    res={}
    for i in t:
        res[i]=res.get(i,0)+1#get方法获得当前字典中该项的value，若没有该项，则默认为0。同时value+1
    return res

def hist(t):#把以上方法汇总，生成字典
    s=cleanpile(t)
    s1=shaixuan(s)
    s2=jishu(s1)
    return s2

def most_common(hist):#对字典中的项以元组的形式导入列表中，生成一个value-key为元组的列表，并按照value进行排序
    t=[]
    for key,value in hist.items():
        t.append((value,key))
    t.sort(reverse=True)#True从大到小，False表示从小到大排序。
    return t

hist=hist(r)#获取字典
t = most_common(hist)#统计排序
print('the most common words are:')
for freq,word in t[:10]:
    print(word,freq,sep='\t')



