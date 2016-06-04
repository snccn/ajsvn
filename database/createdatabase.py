# this is a script that we can build the database file 
# only test on utf8 on windows 
# for python2.7.11 use and support sqlite3

import sqlite3
import os,sys
import tabledesign
import sqltemplate
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
		self.cursor.execute("insert into moeship values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",sql0)
		self.dbconn.commit()
	def getMoeshipinfo(self,id):
		sql="select * from moeship where id="+str(id)+";"
		self.cursor.execute(sql)
		return self.cursor.fetchall()
	def makesqlusetemplate(self,fobj):
		pass

def build():
	reload(sys)
	sys.setdefaultencoding('utf8')
	dbob=dbcontrol()
	#b=a.getMoeshipinfo(1)
	#print b

	#a.addamoeship(sqltemplate.gotdataraw("../data/1.json"))

	# this is the path of the data directory
	# this script only for build the data base it might be never add into the client tools
	for i,j,k in os.walk("../data/"):
		for n in k:
			try:
				dbob.addamoeship(sqltemplate.gotdataraw(i+n))
			except sqlite3.IntegrityError:
				continue
	dbob.dbconn.close()
			#print sqltemplate.gotdataraw(i+n)
if __name__ == '__main__':
	build()


