# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: read_yaml.py
@time: 2019/6/11 22:17
@desc：读取yaml文件
"""
import yaml
import os
from tools.file_path import FilePath


class ReadYaml:
    def __init__(self, path=None):
        self.path = path
        self.file_path = FilePath()
        self.fo = None

    def open_yaml(self):
        """
            读取yamls文件，如果path为空，则读取default.yaml;
            否则读取元素yaml文件
        :return:
        """
        if self.path == None:
            path = self.file_path.yaml_default_file()
        else:
            path = os.path.join(self.file_path.yaml_element_path(), self.path)
        self.fo = open(path, encoding='utf-8')
        data = yaml.load(self.fo)
        return data

    def close_yaml(self):
        self.fo.close()

    def get_default_value(self, host_type, key):
        """获取配置文件内容【default.yaml】"""
        data = self.open_yaml()
        values = data[host_type][key]
        self.close_yaml()
        return values

    def get_element_value(self, key):
        """读取元素文件内容"""
        data = self.open_yaml()
        value = data[key]
        self.close_yaml()
        return value


# r'D:\workspace\auto_ui\yamls\element\govern_base_element.yaml'
# read_yaml = ReadYaml("govern_base_element.yaml")
# print(read_yaml.open_yaml())

