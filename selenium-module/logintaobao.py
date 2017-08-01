# -*- coding: utf-8 -*-

from selenium import webdriver
import time

def test(key,pw):
    url = 'https://login.taobao.com/member/login.jhtml'
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(0.1)
    driver.get(url)
    time.sleep(0.3)
    try:
        driver.find_element_by_xpath("//a[contains(@class,'J_Quick2Static')]").click()
    except Exception as e:
        print(e)
    else:
        time.sleep(0.3)
        driver.find_element_by_xpath("//input[@name='TPL_username']").clear()
        time.sleep(0.1)
        driver.find_element_by_xpath("//input[@name='TPL_password']").clear()
        driver.find_element_by_xpath("//input[@name='TPL_username']").send_keys(key)
        time.sleep(0.1)
        driver.find_element_by_xpath("//input[@name='TPL_password']").send_keys(pw)
        time.sleep(0.1)
        driver.find_element_by_xpath('//*[@id="J_SubmitStatic"]').click()
        time.sleep(5)
    try:
        # 需要手机验证的话
        print('需要进行手机验证码验证，请准备好手机！')
        frame = driver.find_element_by_xpath('//div[@class="login-check-left"]/iframe')
        driver.switch_to.frame(frame)
        time.sleep(0.1)
        driver.find_element_by_xpath('//button[@id="J_GetCode"]').click()
        phone_key = input('请输入验证码：')
        driver.find_element_by_xpath('//input[@id="J_Phone_Checkcode"]').clear()
        driver.find_element_by_xpath('//input[@id="J_Phone_Checkcode"]').send_keys(phone_key)
        time.sleep(1)
        driver.find_element_by_xpath('//input[@type="submit"]').click()
        print('get')
    except:
        print('已经登陆成功，不需要手机验证！')
        # ---------------------------登陆完成-----------------------------
    finally:
        driver.find_element_by_xpath("//span[text()='淘宝网首页']").click()
        print('get')
    time.sleep(200)





if __name__ == '__main__':
    test('','')

