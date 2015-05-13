#!/usr/bin/python
import sys
from module.MeiwenDbHelper import MeiwenDbHelper
import commands
reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == '__main__':
	meiwen = MeiwenDbHelper()
	meiwen.connect()
	content = meiwen.getUnread()
 	meiwen.markread(content['url'])	
	meiwen.close()
	
	output=open('content','w')
	output.write(content['content'])
	output.close()

	commands.getstatusoutput('./msend')		
