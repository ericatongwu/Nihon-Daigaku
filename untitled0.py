#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 11:02:24 2018

@author: wutong
"""
from BeautifulSoup import BeautifulSoup
import urllib2
#import re


# extract URLs of apps 
html = urllib2.urlopen("https://itunes.apple.com/jp/genre/id6005")
soup = BeautifulSoup(html)
li = soup.findAll('li')
print soup.find_all('a')
app_list = li.attrs['href'] # url list
print app_list


# go to the source page
source = []
for url in app_list:
    address = "view-source:" + url
    source.append(address)
    
    
# for each different app, search for the 説明 part
for i in range(len(source)):
    urllib2.urlopen(source[i])
    # insert searching codes
    
    


