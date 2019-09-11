# coding: utf-8
"""
@author: WQ
"""
from __future__ import division  
import nltk, re, pprint
from nltk import word_tokenize
from nltk.data import PathPointer, ZipFilePathPointer, find


#txt在线文档下载
import requests
url = "http://www.gutenberg.org/files/2554/2554.txt"
response = requests.get(url)
raw = response.content.decode('utf8')
print(type(raw))
print(len(raw))
print(raw[:75])


#分词
tokens = word_tokenize(raw)
print(type(tokens))
print(len(tokens))
print(tokens[:10])


#创建text
text = nltk.Text(tokens)
print(type(text))
print(text[1024:1062])
print(text.collocations())


#根据内容定义开始与结尾
print(raw.find("PART I"))
print(raw.rfind("End of Project Gutenberg's Crime"))
raw = raw[5338:1157746]
# raw=raw[raw.find("PART I"):raw.rfind("End of Project Gutenberg's Crime")]
print(raw.find("PART I"))


#HTML下载
url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = requests.get(url).content.decode('utf8')
html[:60]
print(html)

#HTML解析
from bs4 import BeautifulSoup
raw = BeautifulSoup(html,'lxml').get_text()
tokens = word_tokenize(raw)
tokens


bs = BeautifulSoup(html,'lxml')
print(bs.find("div",class_='bodytext').get_text())


#过滤无关内容
tokens = tokens[110:390]
text = nltk.Text(tokens)
text.concordance('gene')
print(text)


#读取本地文件
f = open('d:/data/document.txt','rU')
for line in f:
    print(line.strip())
f.close()


raw = open('d:/data/document.txt').read()
print(type(raw))
tokens = word_tokenize(raw)
print(type(tokens))
words = [w.lower() for w in tokens]
print(type(words))
vocab = sorted(set(words))
print(type(vocab))


vocab.append('blog')
raw.append('blog')

query = 'Who knows?'
beatles = ['john', 'paul', 'george', 'ringo']
query + beatles


#Unicode字符
path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
f= path.open()
for line in f:
    line = line.strip()
    print(line)
f.close()

ord('a')     #计算字符'a'的ASCII码  

a=u'\u0061'  #unicode字符
a

# 编码转换
import unicodedata
lines = path.open( encoding='latin2').readlines()
line = lines[2]
print(line.encode('unicode_escape'))
for c in line: 
     if ord(c) > 127:
         print('%s U+%04x %s'% (c.encode('utf8'), ord(c), unicodedata.name(c)))
lines.close()

# 正则表达式的基本应用
import re
m = re.search(u'\u015b\w*', line)
m.group()
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
#查找ed结尾的词汇
[w for w in wordlist if re.search('ed$', w)]


#字谜：8个字母，第3个字母是j，第6个字母是t
[w for w in wordlist if re.search('^..j..t..$', w)]



#9宫格输入判断
[w for w in wordlist if re.search('^[ghi][mno][jlk][def]$', w)]


#正则表达式中的+
chat_words = sorted(set(w for w in nltk.corpus.nps_chat.words()))
[w for w in chat_words if re.search('^m+i+n+e+$', w)]
[w for w in chat_words if re.search('^[ha]+$', w)]

wsj = sorted(set(nltk.corpus.treebank.words()))
[w for w in wsj if re.search('^[0-9]+\.[0-9]+$', w)]
[w for w in wsj if re.search(r'^[A-Z]+\$$', w)]
[w for w in wsj if re.search('^[0-9]{4}$', w)]
[w for w in wsj if re.search('^[0-9]+-[a-z]{3,5}$', w)]

[w for w in wsj if re.search('^[a-z]{5,}-[a-z]{2,3}-[a-z]{,6}$', w)]

[w for w in wsj if re.search('(ed|ing)$', w)]

#提取字符块
word = 'supercalifragilisticexpialidocious'
print(re.findall(r'[aeiou]', word))
print(len(re.findall(r'[aeiou]', word)))

wsj = sorted(set(nltk.corpus.treebank.words()))
fd = nltk.FreqDist(vs for word in wsj for vs in re.findall(r'[aeiou]{2,}', word))
fd.most_common(12)

regexp = r'^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'
def compress(word):
    pieces = re.findall(regexp, word)
    return ''.join(pieces)

english_udhr = nltk.corpus.udhr.words('English-Latin1')
print(nltk.tokenwrap(compress(w) for w in english_udhr[:75]))

rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')
cvs = [cv for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]', w)]
cfd = nltk.ConditionalFreqDist(cvs)
cfd.tabulate()

cv_word_pairs = [(cv, w) for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]', w)]
cv_index = nltk.Index(cv_word_pairs)
print(cv_index['su'])
print(cv_index['po'])

#查找词干
def stem(word):
    for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
        if word.endswith(suffix):
             return word[:-len(suffix)]
    return word

def stem(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    stem, suffix = re.findall(regexp, word)[0]
    return stem

raw = """DENNIS: Listen, strange women lying in ponds distributing swords
    is no basis for a system of government.  Supreme executive power derives from
    a mandate from the masses, not from some farcical aquatic ceremony."""
tokens = word_tokenize(raw)
[stem(t) for t in tokens]

#搜索已分词文本
from nltk.corpus import gutenberg, nps_chat
moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
print(moby.findall(r"<a> (<.*>) <man>"))
chat = nltk.Text(nps_chat.words())
print(chat.findall(r"<.*> <.*> <bro>")) 
print(chat.findall(r"<l.*>{3,}")) 


from nltk.corpus import brown
hobbies_learned = nltk.Text(brown.words(categories=['hobbies', 'learned']))
hobbies_learned.findall(r"<\w*> <and> <other> <\w*s>")


###规范化文本###
raw = """DENNIS: Listen, strange women lying in ponds distributing swords
    is no basis for a system of government.  Supreme executive power derives from
    a mandate from the masses, not from some farcical aquatic ceremony."""
tokens = word_tokenize(raw)


#词干提取器
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
[porter.stem(t) for t in tokens]
[lancaster.stem(t) for t in tokens]

#词形还原
wnl = nltk.WordNetLemmatizer()
[wnl.lemmatize(t) for t in tokens]


####分句####
text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
sents = nltk.sent_tokenize(text)
pprint.pprint(sents[79:89])

#分词
def segment(text, segs):
    words = []
    last = 0
    for i in range(len(segs)):
        if segs[i] == '1':
            words.append(text[last:i+1])
            last = i+1
    words.append(text[last:])
    return words

text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
seg1 = "0000000000000001000000000010000000000000000100000000000"
seg2 = "0100100100100001001001000010100100010010000100010010000"
segment(text, seg1)
segment(text, seg2)


def evaluate(text, segs):
    words = segment(text, segs)
    text_size = len(words)
    lexicon_size = len(' '.join(list(set(words))))
    return text_size + lexicon_size

text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
seg1 = "0000000000000001000000000010000000000000000100000000000"
seg2 = "0100100100100001001001000010100100010010000100010010000"
seg3 = "0000100100000011001000000110000100010000001100010000001"
print(evaluate(text, seg3))
print(evaluate(text, seg2))
print(evaluate(text, seg1))

from random import randint

def flip(segs, pos):
    return segs[:pos] + str(1-int(segs[pos])) + segs[pos+1:]

def flip_n(segs, n):
    for i in range(n):
        segs = flip(segs, randint(0, len(segs)-1))
    return segs

def anneal(text, segs, iterations, cooling_rate):
    temperature = float(len(segs))
    while temperature > 0.5:
        best_segs, best = segs, evaluate(text, segs)
        for i in range(iterations):
            guess = flip_n(segs, int(round(temperature,0)))
            score = evaluate(text, guess)
            if score < best:
                best, best_segs = score, guess
        score, segs = best, best_segs
        temperature = temperature / cooling_rate
        print(evaluate(text, segs), segment(text, segs))
    print()
    return segs

text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
seg1 = "0000000000000001000000000010000000000000000100000000000"
anneal(text, seg1, 5000, 1.2)
