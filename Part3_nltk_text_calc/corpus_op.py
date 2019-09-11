# -*- coding: utf-8 -*-
"""
@author: WQ
"""
#2.使用语料库模型处理 austen—persuasion.txt。统计整个语料库有多少词标识符？多少词类型
import nltk
nltk.corpus.gutenberg.fileids()
tmp1 = nltk.corpus.gutenberg.words('austen-persuasion.txt')
print(u'词标识符数目：',len(tmp1))       
print(u'词类型数目',len(set(tmp1)))  

#8.在名字语料库上定义一个条件频率分布，显示哪个首字母在男性名字中比在女性名字中更常用
from nltk.corpus import names
cfd = nltk.ConditionalFreqDist(
    (fileid, name[0])
    for fileid in names.fileids()
    for name in names.words(fileid)
)
cfd.plot()

#9.选两个文本， 研究它们之间在词汇、 词汇丰富性、 文体等方面的差异。 
#比较两个文本的词汇量、词汇丰富性
from nltk.book import *

print(len(set(text1)))      # 白鲸记中的词汇量
print(len(set(text2)))      # 理智与情感中的词汇量

def lexical_diversity(text):
    return len(text)/float(len(set(text)))
    
print(lexical_diversity(text1))
print(lexical_diversity(text2))

#统计情态动词can、could、may、might、must、will出现的频数
text_list=[text1,text2]
for text in text_list:
    fdist = nltk.FreqDist([w.lower() for w in text])
    modals = ['can', 'could', 'may', 'might', 'must', 'will']
    print(text)
    for m in modals:
        print(m+':', fdist[m])
#查看白鲸记和情感与理智中的monstrous
text1.similar('monstrous')
text2.similar('monstrous')

text1.similar('pretty')
text2.similar('pretty')



#15. 找出所有在布朗语料库中出现至少3次的词。
from nltk.corpus import brown
text = [w.lower() for w in brown.words() if w.isalpha()]
fdist = nltk.FreqDist(text)
freqList = list(fdist.items())
output = []
for m in freqList:
    if m[1] >= 3:
        output.append(m[0])
print(output)

#17. 找出一个文本中最常出现的50个词，停用词除外
from nltk.corpus import stopwords

def common50(text):
    stopword=stopwords.words('english')
    Dist=FreqDist([w for w in text if w.lower() not in stopword])
    return Dist.most_common()[:50]
    
common50(text1)