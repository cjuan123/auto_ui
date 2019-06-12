# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: chenj
@file: file_path.py
@time: 2019/6/12 14:22
@desc：获取文件路径工具类
"""
import os


class FilePath:

    def root_path(self):
        """获取项目的根路径"""
        path = os.path.abspath(os.path.dirname(__file__)).split('auto_ui')[0]
        root = os.path.join(path, "auto_ui")
        return root

    def yaml_default_file(self):
        """获取项目中的default.yaml文件"""
        yaml_path = os.path.join(self.root_path(), r"yamls\default.yaml")
        return yaml_path

    def yaml_element_path(self):
        """获取项目中的元素yaml文件"""
        yaml_path = os.path.join(self.root_path(), r"yamls\element")
        return yaml_path


# file_path = FilePath()
# print(file_path.yaml_default_file())
# print(file_path.yaml_element_path())