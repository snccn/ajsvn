#!/usr/bin/env python
#thread to read a list in 5 threads
# this code only tested on python2.7.*
import threading
import time
tar=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
flags=0
lock=threading.RLock()
class listread(threading.Thread):
	def __init__(self,name):
		threading.Thread.__init__(self)
		self.name=name
		self.initrd=0.5
		self.stopflag=False
	def run(self):
		global tar,flags
		while not self.stopflag:
			if lock.acquire():
				print tar[flags]
				flags+=1
				lock.release()
			time.sleep(self.initrd)
	def thstop(self):
		self.stopflag=True

if __name__ == '__main__':
	a=[]
	a.append(listread(1))
	a.append(listread(2))
	a.append(listread(3))
	a.append(listread(4))
	a.append(listread(5))
	
	for i in a:
		i.start()
	time.sleep(25)
	for j in a:
		j.thstop()

