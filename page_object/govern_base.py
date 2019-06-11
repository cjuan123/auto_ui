# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: govern_base.py
@time: 2019/6/7 16:43
@desc：政府端登陆
"""
import time
from common.base_page import BasePage
from common.read_yaml import ReadYaml


class GovernLogin(BasePage):

    read_yaml_base = ReadYaml(r'D:\workspace\auto_ui\yamls\element\govern_base_element.yaml')

    def login_info(self, username, password):
        self.send(selector=self.read_yaml_base.get_element_value("user_name"), value=username)
        self.send(selector=self.read_yaml_base.get_element_value("pass_word"), value=password)
        self.click(selector=self.read_yaml_base.get_element_value("login_submit"))

    def switch_groups(self):
        self.click(selector=self.read_yaml_base.get_element_value("switch_groups"))
        time.sleep(1)
        self.click(selector=self.read_yaml_base.get_element_value("button"))


