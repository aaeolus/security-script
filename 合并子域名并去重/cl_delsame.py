#coding=utf-8
import os
import pandas as pd
import glob


def hebing():
    csv_list = glob.glob('*.txt')
    print(u'find %s fle'% len(csv_list))
    print(u'doing............')
    for i in csv_list:
        fr = open(i,'r').read()
        with open('domain.txt','a') as f:
            f.write(fr+"\n")
    print(u'finished')


def quchong(file):
    df = pd.read_csv(file,header=None)
    datalist = df.drop_duplicates()
    datalist.to_csv(file,index=0)   #文件第一行不知道怎么去，手动删吧，notepad++行操作移除空白行

if __name__ == '__main__':
    hebing()
    quchong("domain.txt") 