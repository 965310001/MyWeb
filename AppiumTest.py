#coding:utf-8

from  appium import webdriver
from time import sleep

desired_caps={}
desired_caps["deviceName"]=u"小米平板"
desired_caps["platformVersion"]=u"5.1LMY471"
desired_caps["unicodeKeyboard"]=u"True"
desired_caps["app"]=u"F:\\GitHub\\Python\\MyWeb//baiduyuedu_3900.apk"
desired_caps['appPackage']=u'com.baidu.yuedu'
desired_caps['appActivity']=u'.splash.SplashActivity'
desired_caps['platformName']=u'Android'    #一定要添加这个不然会报错

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
sleep(5)

#个人用户的测试
def testUser():
    global driver

    driver.find_element_by_id('com.baidu.yuedu:id/title_account').click()
    sleep(5)
    #http://www.cnblogs.com/wyx123/articles/4488104.html
    driver.press_keycode(keycode=4)
testUser()

# driver.quit()