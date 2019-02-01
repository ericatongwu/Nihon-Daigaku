#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 14:53:44 2018

@author: wutong
"""


output_words2 = []
unique = []
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')

#f2 = open('result.txt','r')
#file2 = f2.readlines()
for i in range(len(file2)):
    if file2[i] in unique:
        pass
    else:
        unique.append(file2[i])
f2 = open('shuchu.txt','w')
print unique
print len(unique)
wenzhang = ""
for tangou in unique:
    wenzhang += tangou
f2.write(wenzhang)
f2.close()


