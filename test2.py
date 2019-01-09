#!/usr/bin/env python 
# coding=utf-8

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
dr = webdriver.Chrome()
dr.get("https://www.wasu.cn")
#dr.find_element_by_id('searchBtn').click()    #直接点击“搜索”，因为搜索框有默认文案
search = dr.find_element_by_id('search_prompt')  #定位输入框
sleep(3)
search.clear()  #清除默认文案
search.send_keys('黄土高天')  #输入文案
sleep(3)
dr.find_element_by_id('searchBtn').click()  #通过click（）点击搜索
sleep(3)

#获取元素的某些信息
size =dr.find_element_by_id('search_prompt').size #获取输入框元素的尺寸，即宽高
print('输入框尺寸为：',size)

type = dr.find_element_by_id('search_prompt').get_attribute('type')
print('输入框元素的type属性为：',type)


# 定位到要悬停的元素
above = dr.find_elements_by_link_text('登录')

# 对定位到的元素执行鼠标悬停操作
#ActionChains(dr).move_to_element(above).perform()   #注意：由于前面输入框搜索语句的执行，造成页面出现了新TAB页，也就是当前有两个TAB页。而此语句中的ActionChains(dr)，dr还是获取的原始TAB页的DOM结构，所以该语句的执行效果会在第一个TAB页展示，并非是没触发。另外：向百度页面（www.baidu.com)输入框搜索后，虽然页面看似变化了，但始终是一个TAB页，所以界面效果正常。


#dr.quit()
