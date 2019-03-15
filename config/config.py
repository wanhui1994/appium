#coding=utf-8
import configparser

def confset():
    #增加和写入配置文件
    config=configparser.ConfigParser()
    config.read("Confparser.ini")
    config.add_section("desired_caps")
    config.set("desired_caps","platformName","Android")
    config.set("desired_caps","deviceName","ANFNU18130118914")
    config.set("desired_caps","platformVersion","7.0")
    config.set("desired_caps","appPackage","com.faxuan.law")
    config.set("desired_caps","appActivity","com.faxuan.law.app.login.WelcomeActivity")
    config.set("desired_caps","sessionOverride","true")
    config.write(open("Confparser.ini", "w"))
