# -*- coding:utf8 -*-
#release note:
#this is the alpha 0.1 release some bug hasbeen fixed and the basic function supported
#the gui of this application needs waitting
#maybe more function canbe added
import sys,os
try:
	import datacore
	import createdatabase
	import datacore.getIMG
except ImportError:
	sys.path.append("../")
	import datacore
	import createdatabase
	import datacore.getIMG

def getinfo(id):
	selpobj=createdatabase.dbcontrol()
	info=selpobj.getMoeshipinfo(id)
	print info
	pass
def rebuild():
	selpobj=createdatabase.dbcontrol()
	selpobj.createtable()
	createdatabase.build()
	print("build complete")
	pass
def help():
	print "this is the help document"
	print "usage:"
	print "\t\t getinfo    <id>     it can show the infomation of the moe ship using the id"
	print "\t\t rebuild 	        it can rebuild the database and get the update of the value"
	print "\t\t getAssert  <path>   get the Assert files including IMG and IMGBB and so on from the internet*"
	print "\t\t more function just waitting "
	print "\t\t *we get the data from internet and we don't kown the data we get was credible! our data from http://js.ntwikis.com/"
	print u"使用:"
	print u"\t\t getinfo   <id>     可以使用这个对舰娘数据进行查询，提供id就可以"
	print u"\t\t rebuild            使用rebuild来对数据进行重建，必须确定拥有那些json数据"
	print u"\t\t getAssert <path>   使用这个选项来从互联网上获取图片资源 包括正常立绘以及其他图片资料*"
	print u"\t\t 更多功能开发中"
	print u"\t\t *我们从互联网上获取资料,并不保证其可靠性,数据来源: http://js.ntwikis.com/"
def manage(commands):
	reload(sys)
	sys.setdefaultencoding("utf8")
	try:
		if sys.argv[1]=="help":
			help()
		elif sys.argv[1]=="getinfo":
			if len(sys.argv)==3:
				getinfo(sys.argv[2])
			else:
					print "syntax error!"
		elif sys.argv[1]=="rebuild":
			rebuild()
		elif sys.argv[1]=="getAssert":
			datacore.getIMG.getALLPIC(os.getcwd()+os.sep+"assert")
		else:
			print "SyntaxError"
			help()
	except IndexError:
		help()

