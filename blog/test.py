#coding=utf-8
from appium import webdriver
from common.com import Comm
import time,os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Cc():
    p=Comm()
    time.sleep(5)
    def m(self):
        time.sleep(3)
        user_loc = ("xpath","//android.widget.RadioButton[@resource-id='com.faxuan.law:id/rb_mine']")#首页我的
        username_loc = ("id", 'com.faxuan.law:id/et_login_user_name') #登录的用户账号
        password_loc = ("id", 'com.faxuan.law:id/et_login_user_pwd')  #登录的密码
        retrieve_loc = ("id","com.faxuan.law:id/tv_login_find_pwd")   #登录找回密码
        submit_loc = ("id","com.faxuan.law:id/btn_login")              #登录提交按钮
        register_loc = ("id","com.faxuan.law:id/btn_register")         #登录页面的注册按钮
        phone_loc = ("id", 'com.faxuan.law:id/et_login_user_name')    #注册的手机号
        verificationCode_loc = ("id", 'com.faxuan.law:id/et_register_verifi_code') #注册的验证码
        login_loc = ("xpath","//android.widget.TextView[@resource-id='com.faxuan.law:id/tv_name_login']")
        self.p.click(user_loc)
        time.sleep(3)
        self.p.click(login_loc)
        time.sleep(3)
        self.p.send(username_loc,'15011530850')
        self.p.send(password_loc,'123abc')
        self.p.click(submit_loc)
        time.sleep(3)
        sz_loc=('xpath',"//android.widget.ImageView[@resource-id='com.faxuan.law:id/iv_photo']") #点击图片
        self.p.click(sz_loc)
        time.sleep(3)
        tc_loc=('xpath',"//android.widget.TextView[@resource-id='com.faxuan.law:id/btn_take_photo']") #点击拍照
        self.p.click(tc_loc)
        self.p.driver.keyevent(27) #拍照
        time.sleep(2)
        self.p.driver.tap([(942,18),(1038,114)])
        time.sleep(2)
        self.p.driver.tap([(933,0),(1077,144)])




wh=Cc()
wh.m()


