#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
--------------------------------
@File    : pywinauto_examples.py
@Time    : 2019/10/22 14:26
@Author  : Bright Chen
@Mail    : bright_chen7@163.com
--------------------------------
'''

from pywinauto.application import Application
app = Application().start("notepad.exe")

