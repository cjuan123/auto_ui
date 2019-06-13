# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: gover_yang_lao.py
@time: 2019/6/10 11:47
@desc：政府端--养老
"""
from common.base_page import BasePage
from tools.read_yaml import ReadYaml
from time import sleep


class GovernYangLao(BasePage):
    read_yaml = ReadYaml(r'govern_yang_lao_element.yaml')

    def person_click(self):
        """进入人员管理"""
        self.click(selector=self.read_yaml.get_element_value("person"))

    def add_person_click(self):
        """点击添加人员按钮"""
        # self.click(selector=self.read_yaml.get_element_value("left"))
        sleep(1)
        self.click(selector=self.read_yaml.get_element_value("queyr"))
        sleep(1)
        self.click(selector=self.read_yaml.get_element_value("add_person"))


