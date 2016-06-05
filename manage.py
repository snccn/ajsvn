#!/usr/bin/env python
# author snccn
# manage the scripts


import os,sys
import database.manage
import datacore

if __name__ == '__main__':
	database.manage.manage(sys.argv)