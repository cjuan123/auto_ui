# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: gover_house.py
@time: 2019/6/10 11:47
@desc：政府端--适老化
"""
from common.base_page import BasePage
from page_object.govern_house import gover_house_element as house_ele


class GovernHouse(BasePage):

    def resource_manage_click(self):
        self.click(selector=house_ele.resource_manage)

    def agencies_click(self):
        self.click(selector=house_ele.agencies)
