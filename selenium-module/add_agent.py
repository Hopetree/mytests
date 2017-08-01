# -*- coding: utf-8 -*-

import time
from selenium import webdriver

url = "https://httpbin.org/get?show_env=1"

# 将网页滑到最底部
def movepage(driver):
    js_height = '''function test()
            {
            return document.body.clientHeight;
            }
            return test()'''
    k = 1
    height = driver.execute_script(js_height)
    while True:
        if k * 500 < height:
            js_move = "window.scrollTo(0,{})".format(k * 500)
            driver.execute_script(js_move)
            time.sleep(0.2)
            height = driver.execute_script(js_height)
            k += 1
        else:
            break

# 给PJ添加请求头
def test1():
    from selenium.webdriver.common.proxy import Proxy,ProxyType
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    proxy = Proxy({'proxyType':ProxyType.MANUAL,'httpProxy':'http://117.78.51.231:3128'})
    desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
    proxy.add_to_capabilities(desired_capabilities)
    # headers = {
    #     # 'referer':'https://list.tmall.com/',
    #     # 'Host':'https://list.tmall.com',
    #     'Connection':'keep-alive'
    # }
    # dcap = dict(DesiredCapabilities.PHANTOMJS)
    # dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) ")
    # for key,value in headers.items():
    #     dcap['phantomjs.page.customHeaders.{}'.format(key)] = value
    # driver = webdriver.PhantomJS(desired_capabilities=dcap)

    driver = webdriver.PhantomJS(desired_capabilities = desired_capabilities)
    driver.get(url)
    html = driver.page_source
    print(html)

    driver.quit()

# 给谷歌添加请求头
def test2():
    options = webdriver.ChromeOptions()
    options.add_argument('user-agent="Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) "')
    options.add_argument('lang=zh_CN.UTF-8')
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    print(html)

    driver.quit()


if __name__ == '__main__':
    t = time.time()
    test1()
    # test2()

    print("时间 {:.2f}".format(float(time.time()-t)))
