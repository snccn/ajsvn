#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#author snccn
#this is the serializer of the zjsnr and return a list of the data we want 

import json
import time 
import hashlib

def serializer(fileraw):
	handleobj=fileraw
	targetRaw=json.JSONDecoder().decode(fileraw)
	#print targetRaw
	formartoutput(targetRaw)


def formartoutput(targetRaw):
	output=[]
	for i in targetRaw:
		print i
		print targetRaw[i]
		if type(targetRaw[i])==list:
			for j in targetRaw[i]:
				output.append(j)
		elif type(targetRaw[i])==dict:
			output=formartoutput(targetRaw[i])
		else:
			try:
				output.append(targetRaw[i])
				pass
			except:
				print targetRaw[i].encode('utf8')


if __name__ == '__main__':
	fo=open('../data/1007.json','r')
	serializer(fo.read())
