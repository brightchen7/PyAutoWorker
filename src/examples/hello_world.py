#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyautogui
import os
import time

def move_to_center():
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
    pyautogui.alert("alert")
    pyautogui.click()

def runNotepad():
    os.system(u"C:\\Windows\\System32\\notepad.exe")

def runPainter():
    os.system(u"C:\\Windows\\System32\\mspaint.exe")
    time.sleep(3000)

def draw():
    distance = 200
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.5)  # 向右
        distance -= 5
        pyautogui.dragRel(0, distance, duration=0.5)  # 向下
        pyautogui.dragRel(-distance, 0, duration=0.5)  # 向左
        distance -= 5
        pyautogui.dragRel(0, -distance, duration=0.5)  # 向上
    pyautogui.alert("Done!")

# move_to_center()
# runPainter()
draw()