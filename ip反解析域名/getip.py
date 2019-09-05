import re

for line in open("rs.txt"):
    r=re.findall("bilibili.com \((.*\d)\)",line)
    if r!=[]:
    	print r[0]