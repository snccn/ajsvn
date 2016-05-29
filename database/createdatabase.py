# this is a script that we can build the database file 
# only test on utf8 on windows 
# for python2.7.11 use and support sqlite3

import sqlite3
import os
import tabledesign
try:
	import datacore
except ImportError:
	import sys
	sys.path.append('../')
	import datacore

class dbcontrol(object):
	def __init__(self):
		self.dbconn=sqlite3.connect("../moeship.db")
		self.cursor=self.dbconn.cursor()
		self.createtable()
		pass
	def createtable(self):
		sql=tabledesign.CREATE_TABLE
		self.cursor.execute(sql)
		self.dbconn.commit()
	def addamoeship(self,sql0):
		sql=sql0
		self.cursor.execute(sql)
		self.dbconn.commit()  
if __name__ == '__main__':
	a=dbcontrol()
	# this is the path of the data directory
	# this script only for build the data base it might be never add into the client tools
	# for i,j,k in os.walk("../data/"):
	# 	for n in k:
	# 		print i+n

