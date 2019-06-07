# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_baidu.py
@time: 2019/6/7 15:41
@desc：
"""
import unittest
from selenium import webdriver
from page_object.baidu import BaiDu


class TestBaiDu(unittest.TestCase):
    def test_bai_du(self):
        driver = webdriver.Chrome(r"D:\workspace\auto_ui\chromedriver.exe")
        base_page = BaiDu(driver)
        driver.get("http://www.baidu.com")
        driver.implicitly_wait(2)
        base_page.key_send("python")
        driver.implicitly_wait(2)
        base_page.su_click()

        driver.quit()


if __name__ == '__main__':
    unittest.main()