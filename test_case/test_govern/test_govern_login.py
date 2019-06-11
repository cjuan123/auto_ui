# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_govern_login.py
@time: 2019/6/7 16:54
@desc：政府端--适老化登录
"""
import unittest, time, warnings
from common.read_yaml import ReadYaml
from selenium import webdriver
from page_object.govern_base import GovernLogin
from page_object.govern_house.gover_house import GovernHouse


class TestGovernLogin(unittest.TestCase):

    warnings.simplefilter("ignore", ResourceWarning)

    read_yaml = ReadYaml(r'D:\workspace\auto_ui\yamls\default.yaml')
    govern_host = read_yaml.get_default_value("govern", "host")
    user_name = read_yaml.get_default_value("govern", "account")
    pass_word = read_yaml.get_default_value("govern", "password")
    driver = webdriver.Chrome()
    govern_login = GovernLogin(driver=driver)
    govern_house = GovernHouse(driver=driver)

    def setUp(self):
        self.govern_login = GovernLogin(driver=self.driver)
        self.driver.get(self.govern_host + "/Gover")
        self.govern_login.login_info(username=self.user_name, password=self.pass_word)
        time.sleep(3)
        self.govern_login.switch_groups()

    def test_login(self):
        time.sleep(3)
        self.govern_house.agencies_click()

    def tearDown(self):
        # self.driver.quit()
        pass


if __name__ == '__main__':
    unittest.main()

