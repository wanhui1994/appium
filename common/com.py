#coding=utf-8

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from common.mobile_device import Device
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Comm():
     def __init__(self):
         desired_caps=Device()
         self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps.desired('com.faxuan.law','com.faxuan.law.app.login.WelcomeActivity'))

     def WebDriver(self,timeout,method):
         ''' 显示等待'''
         try:
            WebDriverWait(self.driver,timeout,0.5).until(method)
         except Exception as msg:
            print("元素未找到")

     def element(self,locator):
        '''元素定位方法'''
        try:
            element=self.driver.find_element(*locator) # *号是把两个参数分开传值
            return element
        except NoSuchElementException as msg:
            print('元素查找异常：%s'%msg)

     def click(self,locator):
        ''' 点击效果'''
        element = self.element(locator)
        element.click()

     def clea(self,locator):
         element =self.element(locator).clear()
         element.clear()

     def send(self,locator,txt):
        ''' 输入信息'''
        element = self.element(locator)
        # element.clear()
        element.send_keys(txt)

     def swipLeft(self, t=500, n=4):
            '''向左滑动屏幕 t是持续时间 n是滑动次数'''
            l = self.driver.get_window_size()
            x1 = l['width'] * 0.75
            y1 = l['height'] * 0.5
            x2 = l['width'] * 0.25
            for i in range(n):
                self.driver.swipe(x1, y1, x2, y1, t)

     def swipRight(self, t=500, n=4):
            '''向右滑动屏幕'''
            l = self.driver.get_window_size()
            x1 = l['width'] * 0.25
            y1 = l['height'] * 0.5
            x2 = l['width'] * 0.75
            for i in range(n):
                self.driver.swipe(x1, y1, x2, y1, t)

     def swipeUp(self, t=500, n=1):
            '''向上滑动屏幕'''
            l = self.driver.get_window_size()
            x1 = l['width'] * 0.5     # x坐标
            y1 = l['height'] * 0.75   # 起始y坐标
            y2 = l['height'] * 0.25   # 终点y坐标
            for i in range(n):
                self.driver.swipe(x1, y1, x1, y2, t)

     def pohotograph(self,locator,coordinate):
             '''拍照'''
             self.driver.keyevent(27) #拍照
             time.sleep(2)
             self.click(locator) #拍摄图片后的确认操作
             time.sleep(2)
             self.driver.tap(coordinate) #修剪图片的确认操作（使用元素定位失败，故使用模拟手指点击方法进行操作）

     def xzphotos(self):
         '''选择图片'''



