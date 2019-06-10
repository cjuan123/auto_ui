# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: Demo.py
@time: 2019/6/10 11:02
@desc：
"""
from selenium import webdriver

driver = webdriver.Chrome(r"F:\auto_ui\chromedriver.exe")
driver.find_element_by_class_name()
