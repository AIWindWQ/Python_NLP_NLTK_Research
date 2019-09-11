# -*- coding: utf-8 -*-
"""
@author: WQ
"""
import nltk
from nltk.book import  *

#4 在text2中有多少个词？有多少个不同的词？
print(u'text2共有'+str(len(text2))+u'个词')
print(u'text2共有'+str(len(set(text2)))+u'个不同的词')

#5 比较幽默和言情小说的词汇多样性(丰富度)得分，哪一个文体中词汇更丰富？
#幽默
from nltk.corpus import brown
brown.categories()
humor_text = brown.words(categories='humor')

def lexical_diversity(text): 
    return len(text) /float(len(set(text)))

print(u'共有'+str(len(humor_text))+u'个词')
print(u'共有'+str(len(set(humor_text)))+u'个不同的词')
print(u'词汇多样性指标为'+str(lexical_diversity(humor_text)))

#言情
romance_text = brown.words(categories='romance')
print(u'共有'+str(len(romance_text))+u'个词')
print(u'共有'+str(len(set(romance_text)))+u'个不同的词')
print(u'词汇多样性指标为'+str(lexical_diversity(romance_text)))

#7. 查找text5中的搭配
text5.collocations()

#22. 找出聊天语料库中所有4个字母的词，使用频率分布函数以频率高低显示这些词
fdist = FreqDist([w for w in text1 if len(w)==4])
fdist.most_common()[:50]

#28. 定义一个函数percent(word,text),计算一个给定的词在文本中出现的概率，结果以百分比表示
def percent(word,text):
    precent=text.count(word)/float(len(text))
    print(word+u'在文本中的出现频率为'+str(precent*100)+'%')
    
percent('that',text1)