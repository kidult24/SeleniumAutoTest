#!/usr/bin/env python 
# coding=utf-8
from selenium import webdriver
from time import sleep    #导入sleep休眠库

#浏览器控制
dr = webdriver.Chrome()
dr.get("http://www.baidu.com")
print('设置窗口宽480，高800')
dr.set_window_size(480,800)   #适应于移动端页面测试，移动端页面都比PC端小，所以可通过设置对应的宽高来模拟
sleep(3)      #设置休眠时间3s后
dr.maximize_window() #无需传参
sleep(3)
dr.back()  #后退
sleep(3)
dr.forward()  #前进
sleep(3)
dr.refresh() #刷新
sleep(3)
#dr.close() #关闭浏览器当前浏窗口
dr.quit()  #退出浏览器


