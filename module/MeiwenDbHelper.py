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
		self.meiwen = self.conn.netload.meiwen
		
	def markread(self, url):
		self.meiwen.update({'url': url}, {'$set': {'unread': 0}})

	def getUnread(self):
		return self.meiwen.find_one({'unread':1})

	
	def findByUrl(self, url):
		return self.meiwen.find_one({'url':url})
	
	def delete(self, url):
		self.meiwen.remove({'url':url})

if __name__ == '__main__':
	dbHelper = MeiwenDbHelper()
	dbHelper.connect()
	dbHelper.insert("http://test.com", "你好，这是一些测试代码")
	print dbHelper.findByUrl("http://test.com")
	print dbHelper.getUnread()
	dbHelper.markread("http://test.com")
	print dbHelper.findByUrl("http://test.com")
	dbHelper.close()
	
