# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_demo.py
@time: 2019/6/7 15:50
@desc：
"""

from selenium import webdriver
driver = webdriver.Chrome(r"D:\workspace\auto_ui\chromedriver.exe")
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()