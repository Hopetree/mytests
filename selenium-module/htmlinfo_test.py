# -*- coding: utf-8 -*-

from selenium import webdriver
import time

def moveTo():
    '''这个函数可以实现把网页滑到网页最底部，网页中间有加载也能实现完全拉到最下面'''
    url = "https://goelia.tmall.com/shop/view_shop.htm?spm=875.7931836/B.subpannel2016026.1.xpPTAl&user_number_id=133006562&pos=1&acm=2016022913.1003.2.709009&rn=99a403f2b2463b658523cb6694775b4a&scm=1003.2.2016022913.OTHER_1481821973536_709009,test001"
    # driver = webdriver.Chrome()
    driver = webdriver.PhantomJS()
    driver.maximize_window()
    driver.get(url)
    # 返回网页的高度的js代码
    js_height = '''function test()
    {
    return document.body.clientHeight;
    }
    return test()'''
    k = 1
    height = driver.execute_script(js_height)
    while True:
        if k*500 < height:
            js_move = "window.scrollTo(0,{})".format(k * 500)
            driver.execute_script(js_move)
            time.sleep(0.2)
            k += 1
            height = driver.execute_script(js_height)
        else:
            break
    print(k,height)
    driver.save_screenshot("test001.png")


if __name__ == '__main__':
    t = time.time()
    moveTo()
    print("程序耗时：{}秒".format(float(time.time()-t)))