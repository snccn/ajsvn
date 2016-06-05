#!/usr/bin/env python
# -*- coding:utf8 -*-
# this script will aviliable to get the img from the database 
# 
import sqlite3
import sys,os
import shipid
import urllib2,urlparse
URLPOOLimg=[]
URLPOOLimgbb=[]
class getIMG(object):
	def __init__(self):
		self.dbobj=sqlite3.connect("moeship.db")
		self.cur=self.dbobj.cursor()
		pass
	def getPICUrl(self,id):
		global URLPOOL
		sql="select img,img_bb from moeship where id="+str(id)
		#print sql
		self.cur.execute(sql)
		op=self.cur.fetchall()
		#print op
		for i,j in op:
			URLPOOLimg.append(i)
			URLPOOLimgbb.append(j)
		pass
class downloadIMG(object):
	def __init__(self,path,urllist):
		self.path=path
		self.urllist=urllist
		self.sender_header=self.senderheader()
		self.handlethelist()
	def senderheader(self):
		self.host=urlparse.urlsplit(self.urllist[0]).netloc
		#print self.host
		header={
		'Host':self.host,
		'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
		}
		return header
	def createconnobj(self,Url,path):
		connreq=urllib2.Request(Url,headers=self.sender_header)
		try:
			connobj=urllib2.urlopen(connreq)
			data=connobj.read()
			connobj.close()
		except Exception,e:
			data='0'
			return 0
		try:
			fobj=open(path+"\/"+urlparse.urlsplit(Url).path[21:],'wb')
		except:
			os.mkdir(path)
			fobj=open(path+"\/"+urlparse.urlsplit(Url).path[21:],'wb')
		fobj.write(data)
		fobj.close()
	def handlethelist(self):
		for i in self.urllist:
			self.createconnobj(i,self.path)
		pass
def getALLPIC(path):
	#path=".\/Assert"
	testobj=getIMG()
	for j in shipid.ship_all:
		testobj.getPICUrl(j)
	img=downloadIMG(path+os.sep+"IMG",URLPOOLimg)
	img_bb=downloadIMG(path+os.sep+"IMGBB",URLPOOLimgbb)
if __name__ == '__main__':
	print "this script is only for command line use and please use the script named manage.py"
	