# this is the template for execute and insert the data into database 
# from jsonRAW add the json file

import createdatabase
import datacore.serializer

def gotdataraw(filename):
	fobj=open(filename,'r')
	tar=datacore.serializer.serializer(fobj.read())
	print tar

if __name__ == '__main__':
	gotdataraw("../data/100.json")
