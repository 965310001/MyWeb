#-*-coding:utf-8 -*-

import web
import sys


reload(sys)
sys.setdefaultencoding('utf-8')


urls=(
    '/index','Index',
    '/(.*)','GuoFeng'
) #路由


class Index:
    def GET(self):
        # return "郭枫!"
        return web.redirect('a')

class GuoFeng:
    def GET(self,name):
        if not name:
            name='郭枫!!'

        return 'Hello'+name+'!'

if __name__=='__main__':
    web.application(urls,globals()).run()