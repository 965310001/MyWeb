# #coding:utf-8
# import re
# import urllib

# num=175
# htmls=urllib.urlopen("http://www.imooc.com/learn/"+str(num)).read()
#
# # http:\/\/v1.mukewang.com\/e2683b34-157f-4327-99a3-fec22711ac38\/M.mp4
#
# print htmls
#
# urls=re.findall(r"<a href='/video/(\d+)'",htmls,re.M|re.I)
# file_title=re.search('<title>(.*?)</title>',htmls,re.S).group(1).replace("\n","").replace("\r","").replace(" ","").replace('-慕课网','.txt')
#
# print file_title
#
# with open(u'F:\GitHub\Python\Files/{0}'.format(file_title),'w+') as myFile:
#     myFile.write(file_title.replace(".txt","")+"\n\n")
#     for url in urls:
#         myFile.write("http://www.imooc.com/video/"+url+"/M.mp4"+'\n')
#         pass


#电影天堂

# coding:utf-8
import re
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
htmls=urllib.urlopen("http://www.dygod.net/html/tv/oumeitv/20080902/13893.html").read()
for url in re.findall(r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><font color="#ff0000"><a href="(.*?)">',htmls):
    print url.decode('gbk')




# print urllib.urlopen("http://www.uc123.com/").read().decode('utf-8')


with open(r'F:\GitHub\Python\MyWeb\xingnengyouhua.txt','r+',re.M|re.I) as myFile:
    # print myFile.read()
    text=myFile.readlines()
    # for k,v in re.findall(r"链接：(.*?)密码：(.*?)",text):
    #     print k

    # print re.split(r"密码：",text)

    keys={}
    for f in text:
        if f.startswith("链接"):
            # print f
            # keys[re.search('链接：(.*?)密码：',f).group(1)]=re.search('密码：(.*)\n?', f).group(1)
            # print dict(f.replace("链接：","").replace(" 密码：",":"))
            print f.replace("链接：", "'").replace(" 密码：", "':'").replace('\n',"'")

    # for k,v in keys.items():
    #     print k,v

    keys= re.findall(r"链接：(.*?)密码", text)
    values= re.findall(r"密码(.*)\n?", text)
    # print dict(zip(keys,values))




