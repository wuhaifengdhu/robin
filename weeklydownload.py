#!/usr/bin/python
import sys
import re
import urllib2
from bs4 import BeautifulSoup
from module.MeiwenDbHelper import MeiwenDbHelper
import commands
reload(sys)
sys.setdefaultencoding("utf-8")

def getUrls():
	baseurl="http://www.lookmw.cn"
	url=baseurl + "/qingganmeiwen/"
	soup = BeautifulSoup(urllib2.urlopen(url).read())
	links = [ baseurl+link.get('href') for link in soup.find(attrs='weekby mt1').find_all('a')]
	return links

def downloadurl(url):
	soup = BeautifulSoup(urllib2.urlopen(url).read())
	htmldoc = soup.find(attrs="content")
	return re.sub('<[^>]+>','',htmldoc.text)

if __name__ == '__main__':
	urls = getUrls() 
	meiwen = MeiwenDbHelper()
	meiwen.connect()
	for url in urls:
		meiwen.insert(url, downloadurl(url))
	meiwen.close()
		
