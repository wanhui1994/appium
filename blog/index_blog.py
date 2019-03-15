#conding=utf-8
from appium import webdriver
from common.com import Comm

class Index(Comm):
      search_loc = ("xpath", "//android.widget.TextView[@resource-id='com.faxuan.law:id/et_home']") #搜索栏
      law1_loc = ("xpaht","//android.support.v7.widget.RecyclerView[@resource-id='com.faxuan.law:id/recycler_home']/android.widget.LinearLayout[1]/android.widget.ImageView[1]") #分类1
      lawyer_loc = ("xpath","//android.widget.RadioButton[@resource-id='com.faxuan.law:id/rb_lawyer']") #律师
      online_loc = ("xpath","//android.widget.RadioButton[@resource-id='com.faxuan.law:id/rb_processing']") #在线办理
      user_loc = ("xpath","//android.widget.RadioButton[@resource-id='com.faxuan.law:id/rb_mine']") #我的

      def search(self,content):
          self.clea(self.search_loc)
          self.send(self.search_loc,content)  #搜索栏

      def law1(self):
          self.click(self.law1_loc) #进入分类

      def lawyer(self):
          self.click(self.lawyer_loc) #律师

      def onlie(self):
          self.click(self.online_loc) #在线办理

      def user(self):
          self.click(self.user_loc)  #我的

