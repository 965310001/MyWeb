#coding=utf-8

from splinter.browser import Browser
import time


def main():
    baidu=Browser('chrome')
    baidu.visit(r'http://www.baidu.com')
    baidu.find_by_name('wd').fill('Python')
    baidu.find_by_id('su').click()
    time.sleep(10)


if __name__=="__main__":
    main()