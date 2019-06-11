# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: gover_house.py
@time: 2019/6/10 11:47
@desc：政府端--适老化
"""
from common.base_page import BasePage
from common.read_yaml import ReadYaml


class GovernHouse(BasePage):
    read_yaml = ReadYaml(r'D:\workspace\auto_ui\yamls\element\govern_house_element.yaml')

    def agencies_click(self):
        self.click(selector=self.read_yaml.get_element_value("resource_manage"))
        self.click(selector=self.read_yaml.get_element_value("agencies"))


