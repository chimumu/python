import requests
import urllib
import re
import os

def readtxt():

    with open("D:\\ll\\mak.txt",'r') as f:
        a = f.readlines()
        list3 = []
        for j in a:
           lines = j.split()
           list3.append(lines[0])
        return list3


def main():

    r = urllib.request.urlopen('https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/linux-64/')
    a = r.read().decode('utf-8')
    for k in readtxt():
        c = re.compile(r'title="'+k+'.*?</a>')
        b= c.findall(a)

        for i in b:
            w=i.split(">")
            s=w[1].strip("</a")
            print(s)
        """
            lists.append(w)
        
        for j in range(3000,len(lists)):
            list1.append(lists[j])
        
        for k in list1:
            urllib.request.urlretrieve('https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/linux-64/'+k,'E:\\ll\\%s'%k)
    

"""
if  __name__ == '__main__':
    main()
