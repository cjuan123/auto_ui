# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: test_govern_yang_lao.py
@time: 2019/6/7 16:54
@desc：政府端--适老化登录
"""
import unittest, warnings
from tools.read_yaml import ReadYaml
from selenium import webdriver
from tools.logger import Logger
from page_object.govern_base import GovernLogin
from page_object.govern_house.gover_yang_lao import GovernYangLao


class TestGovernLogin(unittest.TestCase):

    warnings.simplefilter("ignore", ResourceWarning)

    log = Logger()

    read_yaml = ReadYaml()
    govern_host = read_yaml.get_default_value("govern", "host")
    user_name = read_yaml.get_default_value("govern", "account")
    pass_word = read_yaml.get_default_value("govern", "password")
    driver = webdriver.Chrome()
    driver.maximize_window()
    govern_login = GovernLogin(driver=driver)
    govern_yang_lao = GovernYangLao(driver=driver)

    @classmethod
    def setUpClass(cls):
        cls.log.info("---------------------------setUpClass--STA-----------------------------")
        cls.govern_login = GovernLogin(driver=cls.driver)
        cls.driver.get(cls.govern_host + "/Gover")
        cls.govern_login.login_info(username=cls.user_name, password=cls.pass_word)

    def test_01_enter_person(self):
        self.log.info("--------enter_person-STA-------")
        self.govern_yang_lao.person_click()
        self.assertEqual("人员信息", self.driver.title)
        self.log.info("--------enter_person-END-------")

    def test_02_add_person(self):
        self.log.info("--------add_person-STA-------")
        self.govern_yang_lao.add_person_click()
        self.log.info("--------add_person-END-------")

    @classmethod
    def tearDownClass(cls):
        # self.driver.quit()
        cls.log.info("---------------------------tearDownClass--END-----------------------------")


if __name__ == '__main__':
    unittest.main()

