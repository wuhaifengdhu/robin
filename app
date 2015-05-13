#!/bin/bash
cd /root/robin
python download.py 
rm ./diandian/content
grep -v '^$' data | grep -v '点点网' >> ./diandian/content
rm data, nowurl
./sendmail
