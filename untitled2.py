#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:15:01 2018

@author: wutong
"""

from BeautifulSoup import BeautifulSoup
import urllib2
import re

html = urllib2.urlopen("https://itunes.apple.com/jp/genre/id6005")
soup = BeautifulSoup(html)
app_link = []
app = " <li><a href=https://itunes.apple.com/jp/app "

for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    if  app in link:
        app_link.append(link)
    else:
        pass

print app_link
        
        
        
        

