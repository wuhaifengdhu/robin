#!/usr/bin/python
#encoding=utf-8

import MongoDBConn

class MeiwenDbHelper:

	dbconn = MongoDBConn.DBConn()
	conn = None
	meiwen = None
	
	def insert(self, url, content):
		self.meiwen.insert([{"url": url, "content": content, "unread": 1}])

	def close(self):
		self.dbconn.close()

	def connect(self):
		self.dbconn.connect()
		self.conn = self.dbconn.getConn()
		self.meiwen = conn.netload.meiwen
		
	def markread(self, url):
		self.meiwen.update({'url': url}, {'$set': {'unread': 0}}, false, false)

	def getUnread(self):
		return self.meiwen.find_one({'unread':1})


	
	
