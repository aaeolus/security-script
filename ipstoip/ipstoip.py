# -*- coding: utf-8 -*-
# __author__ = "lego"
# requirements: IPy
import IPy
import sys

msg = '''
Usage: python ipstoip.py ips.txt
'''

f=open('ip',"w+")

if len(sys.argv) < 2:
    print msg
    exit()
for ips in open(sys.argv[1]):
	ip = IPy.IP(ips)
	for x in ip:
   	    f.writelines(str(x)+'\n')
