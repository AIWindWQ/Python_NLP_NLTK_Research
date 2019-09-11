# -*- coding: utf-8 -*-
"""
@author: WQ
"""
#1
#使用切片符号删除词汇形态上的结尾。例如： 'dogs'[:-1]删除了 dogs的
#最后一个字符，留下 dog。使用切片符号删除下面这些词的词缀
#dish-es, run-ning, nation-ality, un-do, pre-heat
tmp1=['dishes', 'running', 'nationality', 'undo', 'preheat']
print(tmp1[0][:-2])
print(tmp1[1][:3])
print(tmp1[2][:6])
print(tmp1[3][2:])
print(tmp1[4][3:])


#2
#○正则表达式在nlp中的妙用，以下模式是常用的模式可以用来进行文本字符串的提取与过滤：
#a. [a-zA-Z]+           字母字符串
#
#b. [A-Z][a-z]*         开头大写后小字母不限
#
#c. p[aeiou]{,2}t        p开头t结尾中间有<=2个元音字符
#
#d. \d+(\.\d+)?          整数或者小数
#
#e. ([^aeiou][aeiou][^aeiou])*   非元音字母接一个元音字母再接一个非元音字母
#
#f. \w+|[^\w\s]+          \w匹配包括下划线的任何单词字符,等价[A-Za-z0-9_],或匹配非空白符非单词字符的标点符号
import nltk
nltk.re_show(r'[a-zA-Z]+','asdb123')
nltk.re_show(r'[A-Z][a-z]*','asDb123')
nltk.re_show(r'p[aeiou]{,2}t','apaetioo2')
nltk.re_show(r'\d+(\.\d+)?','adf12.34')
nltk.re_show(r'([^aeiou][aeiou][^aeiou])*','papppipe')
nltk.re_show(r'\w+|[^\w\s]+','papppipe?,...')




#3. 格式化字符串
'%6s' %'dog'
'%6s' %'sdasdasdsds'
'%-6s' %'sdasdasdsds'
'%-6s' %'dog'

#4. 将文本转换成hAck3r， 使用正则表达式和替换， 其中 e→3， i→1， o→0， 
#l→|， s→5， .→5w33t!， ate→8。 在转换之前将文本规范化为小写。 
#现在尝试将 s映射到两个不同的值：词开头的s映射为$，词内部的 s映射为5
import re
result=[]
text='say what your classment . ii ate'
words=text.split()


for word in words:
    word=word.lower()
    if 'ate' in word:
        word=word.replace('ate','8')
    elif 'e' in word:
        word=word.replace('e','3')
    if 'i' in word:
        word=word.replace('i','1')       
    if '.' in word:
        word=word.replace('.','5w33t!')
    if 'l' in word:
        word=word.replace('l','|')
    if 'o' in word:
        word=word.replace('o','0')
    if word.startswith('s'):
        word=word.replace(word[0],'$')
    if re.findall(r'^.+s+.+',word)!=[]:
        word=word.replace('s','5')
    result.append(word)       
print(result)

