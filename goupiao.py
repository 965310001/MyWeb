from splinter.browser import Browser
from time import sleep
import traceback

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
        print  u"能做的都做了.....不再对浏览器进行任何操作"
    except Exception as e:
        print(traceback.print_exc())

if __name__ == "__main__":
    huoche()











