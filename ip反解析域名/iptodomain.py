#coding=utf-8
import re
import requests

headers = {'Accept': '*/*',
           'Accept-Language': 'en-US,en;q=0.8',
           'Cache-Control': 'max-age=0',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
           'Connection': 'keep-alive',
           'Referer': 'http://www.baidu.com/'
           }
key=""

#re.findall(r'rel="nofollow" target="_blank">(.*)</a>',r.text)


for ip in open("ip.txt"):
	r=requests.get("https://dns.aizhan.com/"+ip+"/")
	if "bilibili" in r.text:
		print ip+"--> 是bilibili的业务"
	else:
		print ip+"--> 不是bilibili的业务"
