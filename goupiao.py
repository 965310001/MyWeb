#coding:utf8
from splinter.browser import Browser
from time import sleep
import traceback

starts = u"%u5E7F%u5DDE%2CGZQ"
#吉安
ends = u"%u5409%u5B89%2CVAG"
#北京
# ends = u"%u5317%u4EAC%2CBJP"

username="15949629529"
passwd="kui123456kui"

# username="zhouqing19931214"
# passwd="zq15216235198"

ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
login_url = "https://kyfw.12306.cn/otn/login/init"
initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"

order = 0
dtime = "2017-01-21"

pa = u"郭远逵"
# pa = u"周青"

def login():
    b.find_by_text(u"登录").click()
    sleep(3)
    b.fill("loginUserDTO.user_name", username)
    sleep(1)
    b.fill("userDTO.password", passwd)
    sleep(1)
    print u"等待验证码，自行输入..."
    while True:
        if b.url != initmy_url:
            sleep(1)
        else:
            break

def goWhild():
    try:
        print u"购票页面..."
        # 跳回购票页面
        b.visit(ticket_url)

        # 加载查询信息
        b.cookies.add({"_jc_save_fromStation": starts})
        b.cookies.add({"_jc_save_toStation": ends})
        b.cookies.add({"_jc_save_fromDate": dtime})
        b.reload()

        sleep(2)

        count = 0
        # 循环点击预订
        if order != 0:
            while b.url == ticket_url:
                b.find_by_text(u"查询").click()
                count += 1
                print u"循环点击查询... 第 %s 次" % count
                sleep(3)
                try:
                    b.find_by_text(u"预订")[order - 1].click()
                except:
                    print u"还没开始预订"
                    continue
        else:
            while b.url == ticket_url:
                b.find_by_text(u"查询").click()
                count += 1
                print u"循环点击查询... 第 %s 次" % count
                sleep(3)
                try:
                    for i in b.find_by_text(u"预订"):
                        i.click()
                except:
                    print u"还没开始预订"
                    continue
        sleep(1)
        b.find_by_text(pa)[1].click()
        sleep(5)
        b.find_by_id(u"submitOrder_id").click()
        b.find_by_id(u"qr_submit_id").click()
        print  u"能做的都做了.....不再对浏览器进行任何操作"
    except Exception as e:
        goWhild()
        print(traceback.print_exc())

def huoche():
    global b
    b = Browser(driver_name="chrome")
    b.visit(ticket_url)

    while b.is_text_present(u"登录"):
        sleep(1)
        login()
        if b.url == initmy_url:
            break

    try:
        print u"购票页面..."
        # 跳回购票页面
        b.visit(ticket_url)

        # 加载查询信息
        b.cookies.add({"_jc_save_fromStation": starts})
        b.cookies.add({"_jc_save_toStation": ends})
        b.cookies.add({"_jc_save_fromDate": dtime})
        b.reload()

        sleep(2)

        count = 0
        # 循环点击预订
        if order != 0:
            while b.url == ticket_url:
                b.find_by_text(u"查询").click()
                count +=1
                print u"循环点击查询... 第 %s 次" % count
                sleep(1)
                try:
                    b.find_by_text(u"预订")[order - 1]
                    b.find_by_id(r"YW_65000K422304")
                    b.find_by_text(u"预订")[order - 1].click()
                except:
                    print u"还没开始预订"
                    continue
        else:
            while b.url == ticket_url:
                b.find_by_text(u"查询").click()
                count += 1
                print u"循环点击查询... 第 %s 次" % count
                sleep(1)
                try:
                    for i in b.find_by_text(u"预订"):
                        i.click()
                except:
                    print u"还没开始预订"
                    continue
        sleep(1)
        b.find_by_text(pa)[1].click()
        sleep(1)
        b.find_by_id(u"submitOrder_id").click()
        b.find_by_id(u"qr_submit_id").click()
        print  u"能做的都做了.....不再对浏览器进行任何操作"

    except Exception as e:
        print ('退出中')
        print(traceback.print_exc())

if __name__ == "__main__":

    for i in range(11):
        print ((i + 52.8)*5 - 3.9343) / 0.5 - i * 10

    # huoche()