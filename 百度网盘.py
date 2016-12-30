#coding:utf-8

import re
from splinter.browser import Browser
from time import sleep
import traceback

with open(r'F:\GitHub\Python\MyWeb\xingnengyouhua.txt','r+',re.M|re.I) as myFile:
    text=myFile.readlines()
    keys={}
    for f in text:
        if f.startswith("链接"):
            keys[re.search(r'链接：(.*?)密码：',f).group(1)]=re.search(r'密码：(.*)\n?', f).group(1)
            # print dict(f.replace("链接：","").replace(" 密码：",":"))
            # print f.replace("链接：", "'").replace(" 密码：", "':'").replace('\n',"'")

    for k,v in keys.items():
        print k,v

b = Browser(driver_name="chrome")
b.visit(u'http://pan.baidu.com/share/init?shareid=271013996&uk=2801866203 ')

        # sleep(100000000)

