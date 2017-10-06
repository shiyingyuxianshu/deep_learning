# 上交作业的时候，才发现自己理解错误了，向WhaleChen学习了相关内容
# 打开文件，读取文件
with open('./happiness_seg.txt') as f:
    file = f.read()

import collections

filelist = file.split()
filelist2 = list()
for i in range(len(filelist)-1):
    #定义每个独立的词即为 长度需要至少为2的词
    #当然，这可能是一种过度的简化
    #这样的好处是对于标点符号也自然被去除 
    if (len(filelist[i]) > 1 and len(filelist[i+1]) > 1):
        filelist2.append(filelist[i] +" "+ filelist[i+1])
#使用 Counter函数，便于统计
frequency = collections.Counter(filelist2)

print(frequency.most_common(10))