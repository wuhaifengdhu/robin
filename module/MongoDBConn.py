#!/usr/bin/python
#encoding=utf-8

import pymongo

class DBConn:
	conn = None
	server = "mongodb://localhost:27017"

	def connect(self):
		self.conn = pymongo.Connection(self.servers)

	def close(self):
		return self.conn.disconnect()
	
	def getConn(self):
		return self.conn
