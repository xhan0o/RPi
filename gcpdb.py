#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Copyright © 2017 tars <tars@TARS>
# Distributed under terms of the MIT license.

#Code to communicate with google cloud database directly.


'''
Usage: gcpdb.gcppost([data])
[data] - List
'''

import MySQLdb
from datetime import datetime


gcpdb = MySQLdb.connect(host="IP", user="USER", passwd="PASSWORD")


cur=gcpdb.cursor()
def gcppost(data):
    	cur.execute("use test;") #use 'DatabaseName'
	#Create table and columns 
	cur.execute("create table IF NOT EXISTS datastore (timestamp varchar(40),chan varchar(4),meassure varchar(20),qp varchar(20),qn varchar(20), T3 varchar(20), T1 varchar(20),sspeed varchar(20),sendflag varchar(20));")
    	#Insert the data
	cur.execute("insert into datastore (timestamp,chan,meassure,qp,qn,T3,T1,sspeed,sendflag) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],"Posted"))
    	#Commit (save)
	gcpdb.commit()
    	#print "done" #Debug
	return
