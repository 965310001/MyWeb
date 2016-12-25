#coding:utf-8

import urllib,urllib2,json

url='http://apis.baidu.com/qunar/qunar_train_service/traindetail'
data={'version':'1.0',
      'train':'G101',
      'from':'北京南',
      'to':'上海虹桥',
      'date':'2016-12-18'}
datas=urllib.urlencode(data)
req=urllib2.Request(url,data)
req.add_header('apikey','bdb80cb2ae4071370edbcf57a982fa0d')
resp=urllib2.urlopen(req,datas)
html=resp.read().decode('utf-8')

print (html,'\n',resp.url)
def json_jx(html):
    train_list=json.loads(html)
    return train_list

json_html=json_jx(html)
# print (json_html['data']['trainNo'])
# print (json_html['data']['dptStation'])
# print (json_html['data']['arrStation'])
# print (json_html['data']['dptDate'])
# print (json_html['data']['typeName'])

print ('--------------------------------------------')
# print (json_html)
# print (json_html['data']['s2sBean'])
# print (json_html['data']['s2sBean']['seats'].keys)


print ('|||||||||||||||||||||||||||||||||||||||||||||||||||||')

def dictItems(json_html):

    for (k, v) in json_html.items():
        if type(v)==dict:
            print k
            dictItems(v)
        elif type(v)==list:
            for item in v:
                print item
        else:
            print k,':',v
dictItems(json_html)

'''
print (type(json_html['data']['s2sBean']['seats']))

for (k,v) in json_html['data']['s2sBean']['seats'].iteritems():
    print k,v

for (k,v) in json_html['data']['s2sBean']['seats'].items():
    print k
    for (itemk,itemv) in v.iteritems():
        print itemk,':',itemv
    print ''
'''