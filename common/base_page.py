# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: base_page.py
@time: 2019/6/7 0:10
@desc：元素定位方法
"""


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, selector):
        """元素定位方法"""
        self.driver.implicitly_wait(10)  # 隐式等待
        by = selector[0]
        value = selector[1]
        element = None
        if by == "id" or by == "name" or by == "link" or by == "xpath" or by == "class":
            if by == "id":
                element = self.driver.find_element_by_id(value)
            elif by == "name":
                element = self.driver.find_element_by_name(value)
            elif by == "link":
                element = self.driver.find_element_by_link_text(value)
            elif by == "xpath":
                element = self.driver.find_element_by_xpath(value)
            elif by == "class":
                element = self.driver.find_element_by_class_name(value)
            else:
                print("没有找到元素，请检查！！")
            return element
        else:
            print("元素定位错误！！")

    def send(self, selector, value):
        """输入值"""
        element = self.find_element(selector=selector)
        try:
            element.send_keys(value)
            print("元素输入内容：%s" % value)
        except Exception:
            print("Exception error")

    def click(self, selector):
        """点击事件"""
        element = self.find_element(selector=selector)
        element.click()

    def script_scroll(self):
        """#向下滚动到页面底部  """
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")
