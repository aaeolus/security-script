import re
f = open("file.txt","r")
rs = open("rs.txt","w+")
ip = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",f.read())
for i in ip:
	rs.write(i+'\n')