ip=[]
for line in open("srcip.txt"):
	line=line.replace("\n","")
	if line not in ip:
		ip.append(line)
		print line