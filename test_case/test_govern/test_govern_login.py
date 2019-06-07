# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_govern_login.py
@time: 2019/6/7 16:54
@desc：政府端--登录
"""
import unittest
from common import DEFAULT
from selenium import webdriver
from page_object.test_govern.govern_login import GovernLogin


class TestGovernLogin(unittest.TestCase):

    govern_host = DEFAULT.government_host

    def test_login(self):
        driver = webdriver.Chrome(r"D:\workspace\auto_ui\chromedriver.exe")
        govern_login = GovernLogin(driver=driver)
        driver.get(self.govern_host + "/Gover")
        govern_login.user_name_key("")
        govern_login.pass_word_key("")
        govern_login.login_submit()
        driver.quit()


if __name__ == '__main__':
    unittest.main()

