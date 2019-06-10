# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_govern_login.py
@time: 2019/6/7 16:54
@desc：政府端--适老化登录
"""
import unittest
import time
import warnings
from common import DEFAULT
from selenium import webdriver
from page_object.govern_base import GovernLogin
from page_object.govern_house.gover_house import GovernHouse


class TestGovernLogin(unittest.TestCase):

    govern_host = DEFAULT.government_host

    warnings.simplefilter("ignore", ResourceWarning)
    driver = webdriver.Chrome()
    govern_login = GovernLogin(driver=driver)
    govern_house = GovernHouse(driver=driver)

    def setUp(self):
        self.govern_login = GovernLogin(driver=self.driver)
        self.driver.get(self.govern_host + "/Gover")
        self.govern_login.user_name_key("")
        self.govern_login.pass_word_key("123qwe")
        self.govern_login.login_submit()
        self.govern_login.switch_groups()
        time.sleep(3)
        self.govern_login.button_click()

    def test_login(self):
        time.sleep(3)
        self.govern_house.resource_manage_click()
        self.govern_house.agencies_click()

    def tearDown(self):
        # self.driver.quit()
        pass


if __name__ == '__main__':
    unittest.main()

