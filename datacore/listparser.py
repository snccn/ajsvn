#!/usr/bin/env python
#-*- Coing:utf8 -*-
# how about handle the html files

import HTMLParser

class handlelist(HTMLParser.HTMLParser):
	def __init__(self,dataw):
		HTMLParser.HTMLParser.__init__(self)
		self.raw=[]
		self.load(dataw)
	def handle_starttag(self,tag,attrs):
		if tag=='a':
			for (variable,value) in attrs:
				if variable=='href':
					if value != '#':
						self.raw.append(value)
	def load(self,dataw):
		self.feed(dataw)

if __name__ == '__main__':
	fo=open('list.html','r')
	ta=fo.read()
	#print ta
	taret=handlelist(ta)
	#print taret.raw
	for i in taret.raw:
		print i[52:]