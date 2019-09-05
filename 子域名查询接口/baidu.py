#coding=utf-8
import requests
import sys
import json

domain = "myoas.com"
#domain = sys.argv[1]
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}



url="http://ce.baidu.com/index/getRelatedSites?site_address=%s"%(domain)

r = requests.get(url,headers=headers)
rs=json.loads(r.text)

file = open("baidu_rs.txt","w+")
for son_domain in rs['data']:
 	file.write(son_domain["domain"]+"\n")

file.close()

