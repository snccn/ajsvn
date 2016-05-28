#!/usr/bin/env python
# -*- Coding:utf8 -*-
# author snccn
# formart the data from json file witch datacore get
# date 201605061439
import json
import time
class decodeandreturnstring(object):
	def __init__(self,listRAW):
		self.raw=listRAW
		self.output=[]
		self.temp=[]
		self.decoderaw={}
	def jsTodict(self):
		jsondecode=JSONDecoder().decode(self.raw)

