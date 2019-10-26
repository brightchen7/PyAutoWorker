#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
--------------------------------
@File    : cursorFecther.py
@Time    : 2019/10/13 18:25
@Author  : Bright Chen
@Mail    : bright_chen7@163.com
--------------------------------
'''

import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')