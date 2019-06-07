# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: baidu.py
@time: 2019/6/7 15:36
@desc：
"""
from common.base_page import BasePage


class BaiDu(BasePage):
    kw = ["id", "kw"]
    su = ["id", "su"]

    def key_send(self, value):
        self.send(self.kw, value=value)

    def su_click(self):
        self.click(self.su)
