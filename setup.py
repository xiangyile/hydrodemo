"""
Author: Wenyu Ouyang
Date: 2022-06-28 21:29:43
LastEditTime: 2022-06-28 21:54:23
LastEditors: Wenyu Ouyang
Description: setup file
FilePath: \hydro-test\setup.py
Copyright (c) 2021-2022 Wenyu Ouyang. All rights reserved.
"""
#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "hydrotest", # 输入项目名称
    version = "0.0.1", # 输入版本号
    keywords = ["test"], # 输入关键词
    description = "hydro test", # 输入概述
    long_description = "a test repo for pypi packaging", # 输入描述

    url = "https://github.com/OuyangWenyu/hydro-test", # 输入项目Github仓库的链接
    author = "Wenyu Ouyang", # 输入作者名字
    author_email = "wenyuouyang@outlook.com", # 输入作者邮箱
    license= "MIT_license", # 此为声明文件，一般填写 MIT_license

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["numpy"], # 输入项目所用的包
    python_requires='>=3.9', # Python版本要求
)
