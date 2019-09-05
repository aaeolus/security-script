#coding=utf-8
import requests
import sys
import json

domain = "acg.tv"
#domain = sys.argv[1]
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}



url="https://www.virustotal.com/vtapi/v2/domain/report?apikey=8b97303d0152e516b5961bf70a1fb8cd3313d1686f3a46d8d72d1ca828fde45f&domain=%s"%(domain)

r = requests.get(url,headers=headers)
rs=json.loads(r.text)

file = open("virustotal_rs.txt","w+")
for son_domain in rs['subdomains']:
	file.write(son_domain+"\n")

file.close()

