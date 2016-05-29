# this is the template for execute and insert the data into database 
# from jsonRAW add the json file

import createdatabase,os,sys
try:
	import datacore.serializer
except ImportError:
	sys.path.append("../")
	import datacore.serializer
import sys
def gotdataraw(filename):
	fobj=open(filename,'r')
	tar=datacore.serializer.serializer(fobj.read())
	value=(tar['ID'],tar['NAME'],tar['STARS'],tar['WEDDING_TALK'],tar['DESC'],tar['TYPE'],tar['NI_CHENG'],tar['GETTING_TALK'],tar['SHE_CHENG'],tar['PIN_YIN'],
		tar['DAN'],tar['YOU'],tar['LIFE'],tar['LIFE_MAX'],tar['SHAN_BI'],tar['SHAN_BI_MAX'], tar['DEFENCE'],tar['DEFENCE_MAX'],
		tar['NO'],tar['OIL_COST'],tar['GANG_COST'],tar['ZHEN_CHA'],tar['ZHEN_CHA_MAX'],tar['NATION'],tar['DA_ZAI'],tar['FEN_BU'],
		tar['SU_DU'],tar['ROCKETS'],tar['ROCKETS_MAX'],tar['ID']+1000,tar['GAI_ZAO'],str(tar['IS_OPENED']),tar['BUILD_TIME'],tar['WEAPON'],
		tar['IMG_BN'],tar['IMG_BB'],str(tar['FOCUS']),)
	# print tar['ID']
	# print tar['NAME']
	# print tar['STARS']
	# print tar['WEDDING_TALK']
	# print tar['DESC']
	# print tar['TYPE']
	# print tar['NI_CHENG']
	# print tar['GETTING_TALK']
	# print tar['SHE_CHENG']
	# print tar['PIN_YIN']
	# print tar['DAN']
	# print tar['YOU']
	# print tar['LIFE']
	# print tar['LIFE_MAX']
	# print tar['SHAN_BI']
	# print tar['SHAN_BI_MAX']
	# print tar['DEFENCE']
	# print tar['DEFENCE_MAX']
	# print tar['NO']
	# print tar['OIL_COST']
	# print tar['GANG_COST']
	# print tar['ZHEN_CHA']
	# print tar['ZHEN_CHA_MAX']
	# print tar['NATION']
	# print tar['DA_ZAI']
	# print tar['FEN_BU']
	# print tar['SU_DU']
	# print tar['ROCKETS']
	# print tar['ROCKETS_MAX']
	# print tar['ID']+1000
	# print tar['GAI_ZAO']
	# print tar['IS_OPENED']
	# print tar['BUILD_TIME']
	# print tar['WEAPON']
	# print tar['IMG_BN']
	# print tar['IMG_BB']
	# print tar['FOCUS']
	#print tar['MAX_DATA']
	# print len(value)
	return value

def combine(value):
	sql="insert into moeship values "
	print sql
	return sql
if __name__ == '__main__':
	#this is the start of the complete
	reload(sys)
	sys.setdefaultencoding('utf8')
	
	combine(gotdataraw("../data/100.json"))
