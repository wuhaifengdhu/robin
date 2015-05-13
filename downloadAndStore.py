#!/usr/bin/python
import sys
import re
import urllib2
from bs4 import BeautifulSoup
import commands
reload(sys)
sys.setdefaultencoding("utf-8")
commands.getstatusoutput('./download_url')
url=commands.getstatusoutput('cat nowurl')[1]
soup = BeautifulSoup(urllib2.urlopen(url).read())
htmldoc=soup.find_all(attrs=re.compile("rich-content"))
txt=""
for con in htmldoc:
	txt=txt+re.sub('<[^>]+>','',con.text)	
print txt
output=open('data','w')
output.write(txt)
output.close()
