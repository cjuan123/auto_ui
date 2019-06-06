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
        by = selector[0]
        value = selector[1]
        element = None
        if by == "id" or by == "name" or by == "link" or by == "xpath":
            if by == "id":
                element = self.driver.find_element_by_id(value)
            elif by == "name":
                element = self.driver.find_element_by_name(value)
            elif by == "link":
                element = self.driver.find_element_by_link_text(value)
            elif by == "xpath":
                element = self.driver.find_element_by_xpath(value)
            else:
                print("没有找到元素，请检查！！")
            return element
        else:
            print("元素定位错误！！")

    def send(self, selector, value):
        """输入值"""
        element = self.find_element(selector=selector)
        try:
            element.send_key(value)
            print("元素输入内容：%s" % value)
        except Exception:
            print("error")

    def click(self, selector):
        """点击事件"""
        element = self.find_element(selector=selector)
        element.click()
