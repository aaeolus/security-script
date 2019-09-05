import requests



for ip in open("ip.txt"):
	url="https://"+ip.replace("\n", "")
	try:
		r=requests.get(url)
	except Exception,e:
		if "bilibili" in str(e):
			print(ip+"is belong to bilibili")
		else:
			print("no belong")