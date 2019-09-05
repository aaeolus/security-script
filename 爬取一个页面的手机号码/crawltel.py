#coding=utf-8
import re
import requests
import sys

msg = '''
Usage: python -u http://www.test.com/1.html
'''

def gethtml(url):
	html=requests.get(url).content
	tel = re.findall("\d{11}",html)
	return tel
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print msg
		exit()
	else:
		url=sys.argv[2]
		tels=gethtml(url)
		for i in tels:print(i)