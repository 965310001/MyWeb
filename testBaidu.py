#coding:utf-8

from splinter.browser import Browser
from time import sleep
import traceback

# import os
# from selenium import webdriver
# chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
# os.environ["webdriver.chrome.driver"] = chromedriver
# driver =  webdriver.Chrome(chromedriver)
# driver.get("http://stackoverflow.com")
# driver.quit()

import os
from selenium import webdriver

def main():
    browser = Browser("chrome")
    browser.visit('http://www.baidu.com')

    # chromedriver = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    # os.environ["webdriver.chrome.driver"] = chromedriver
    # driver =  webdriver.Chrome(chromedriver)
    # # driver.maximize_window()
    # driver.get("https://www.baidu.com/")
    # print(driver.title)
    # driver.quit()


if __name__=="__main__":
    print ("测试开始")
    main()
    print ("测试结束")

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import os, time
#
# driver = webdriver.Chrome()
# driver.get("www.baidu.com")
#
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.start()
