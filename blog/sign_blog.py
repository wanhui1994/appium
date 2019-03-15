#condig=utf-8

from common.com import Comm

class Sign(Comm):
    username_loc = ("id", 'com.faxuan.law:id/et_login_user_name') #登录的用户账号
    password_loc = ("id", 'com.faxuan.law:id/et_login_user_pwd')  #登录的密码
    retrieve_loc = ("id","com.faxuan.law:id/tv_login_find_pwd")   #登录找回密码
    submit_loc = ("id","com.faxuan.law:id/btn_login")              #登录提交按钮
    register_loc = ("id","com.faxuan.law:id/btn_register")         #登录页面的注册按钮
    phone_loc = ("id", 'com.faxuan.law:id/et_login_user_name')    #注册的手机号
    verificationCode_loc = ("id", 'com.faxuan.law:id/et_register_verifi_code') #注册的验证码



    def input_name(self,name):
        '''输入用户账号'''
        self.send(self.username_loc,name)

    def input_pass(self,password):
        '''输入密码'''
        self.send(self.password_loc,password)

    def input_phone(self,phone):
        '''输入注册时的手机号'''
        self.send(self.phone_loc,phone)

    def input_code(self,code):
        '''输入注册时的验证码'''
        self.send(self.verificationCode_loc,code)

    def click_retrieve(self):
        '''找回密码'''
        self.click(self.retrieve_loc)

    def click_submit(self):
        '''点击登录按钮'''
        self.click(self.click_submit)

    def click_register(self):
        '''注册新账号'''
        self.click(self.register_loc)

    def login(self,name,password):
        self.input_name(name)
        self.input_pass(password)
        self.click_submit()


