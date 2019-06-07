# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: govern_login.py
@time: 2019/6/7 16:43
@desc：政府端登陆
"""
from page_object.test_govern import govern_login_element as g_login
from common.base_page import BasePage


class GovernLogin(BasePage):

    def user_name_key(self, value):
        self.send(selector=g_login.user_name, value=value)

    def pass_word_key(self, value):
        self.send(selector=g_login.pass_word, value=value)

    def login_submit(self):
        self.click(selector=g_login.login_submit)

