# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_govern_yang_lao.py
@time: 2019/6/7 16:54
@desc：政府端--适老化登录
"""
import unittest, time, warnings
from common.read_yaml import ReadYaml
from selenium import webdriver
from page_object.govern_base import GovernLogin
from page_object.govern_house.gover_yang_lao import GovernYangLao


class TestGovernLogin(unittest.TestCase):

    warnings.simplefilter("ignore", ResourceWarning)

    read_yaml = ReadYaml()
    govern_host = read_yaml.get_default_value("govern", "host")
    user_name = read_yaml.get_default_value("govern", "account")
    pass_word = read_yaml.get_default_value("govern", "password")
    driver = webdriver.Chrome()
    driver.maximize_window()
    govern_login = GovernLogin(driver=driver)
    govern_yang_lao = GovernYangLao(driver=driver)

    def setUp(self):
        self.govern_login = GovernLogin(driver=self.driver)
        self.driver.get(self.govern_host + "/Gover")
        self.govern_login.login_info(username=self.user_name, password=self.pass_word)

    def test_01_enter_person(self):
        self.govern_yang_lao.person_click()
        self.assertEqual("人员信息", self.driver.title)

    def test_02_add_person(self):
        self.govern_yang_lao.add_person_click()
        # self.assertEqual("新增人员", self.driver.title)


    @classmethod
    def tearDownClass(cls):
        # self.driver.quit()
        pass


if __name__ == '__main__':
    unittest.main()

