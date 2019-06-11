# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: read_yaml.py
@time: 2019/6/11 22:17
@desc：读取yaml文件
"""
import yaml


class ReadYaml:
    def __init__(self, path):
        self.path = path

    def open_yaml(self):
        f = open(self.path, encoding='utf-8')
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data

    def get_default_value(self, host_type, key):
        data = self.open_yaml()
        values = data[host_type][key]
        return values

    def get_element_value(self, key):
        data = self.open_yaml()
        value = data[key]
        return value


# read_yaml = ReadYaml(r'D:\workspace\auto_ui\yamls\element\govern_base_element.yaml')
# print(read_yaml.get_element_value("pass_word"))

