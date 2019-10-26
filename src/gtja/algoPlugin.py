#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
--------------------------------
@File    : algoPlugin.py
@Time    : 2019/10/13 15:43
@Author  : Bright Chen
@Mail    : bright_chen7@163.com
--------------------------------
'''

import pyautogui
import time
from datetime import datetime
import arrow

ticker_x, ticker_y = 380, 165
sell1_x, sell1_y = 660, 276
buy1_x, buy1_y = 660, 304
last_x, last_y = 606, 453
price_x, price_y = 390, 260
qty_x, qty_y = 420, 353
order_x, order_y = 423, 511
qty_normal_x, qty_normal_y = 420, 345
order_normal_x, order_normal_y = 423, 485

'''
send order to simulat48e UI control

@TODO: exception case for error
'''
def send_order(ticker, qty, limit_price="last", type="margin"):
    # set ticker
    update_number(ticker_x, ticker_y, ticker)
    # set price
    if limit_price == 'last':
        pyautogui.moveTo(last_x, last_y)
        pyautogui.click()
    elif limit_price == 'sell':
        pyautogui.moveTo(sell1_x, sell1_y)
        pyautogui.click()
    else:
        update_number(price_x, price_y, str(limit_price))
    if type == "margin":
        # set quantity
        update_number(qty_x, qty_y, str(qty))
        # send order
        pyautogui.moveTo(order_x, order_y, 0.25)
        pyautogui.click()
    elif type == "normal":
        # set quantity
        update_number(qty_normal_x, qty_normal_y, str(qty))
        # send order
        pyautogui.moveTo(order_normal_x, order_normal_y, 0.25)
        pyautogui.click()
    else:
        print("type error: " + type)
        exit(0)
    # waiting for message box
    time.sleep(1)
    # confirm
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("enter")

def update_number(x_position, y_position, update_num):
    pyautogui.moveTo(x_position, y_position, 0.25)
    pyautogui.doubleClick()
    pyautogui.press('delete')
    pyautogui.typewrite(update_num)

def simulate_order(ticker, qty, limit_price="last"):
    output_str = "%s: ticker: %s, qty:%s, price:%s" % (str(datetime.now()), ticker, qty, limit_price)
    print(output_str)

'''
Time-Weighted Average Price
@start_time  : the time for the algo start
@end_time    : the time for the end point
@duration    : send order immediately by specific minutes
@interval    : the minimize time interval for the order
@price       : the price send to market
'''
def twap(ticker, quantity, duration=30.0, start_time=None, end_time=None, interval=0.0, price="LAST", volume_pct=0.33, min_size=1000, type="margin"):
    second_num = 0
    if start_time != None and end_time != None:
        start_arrow = arrow.get(start_time, "HH:mm:ss")
        end_arrow = arrow.get(end_time, "HH:mm:ss")
        second_num = (end_arrow - start_arrow).seconds
        now_time = arrow.now()
        while start_time != now_time.format("HH:mm:ss"):
            time.sleep(1)
            print("waiting for start time: %s" % str(now_time))
            now_time = arrow.now()
    else:
        if duration != None:
            start_arrow = arrow.now()
            end_arrow = arrow.get("14:56:55", "HH:mm:ss")
            market_close_seconds = (end_arrow - start_arrow).seconds
            second_num = min(market_close_seconds, int(duration * 60))
        else:
            print('incorrect time parameter for execution: either specific time or duration')
            return None
    if second_num < 5:
        print("too short time")
        return None
    print("total number: " + str(second_num))
    remain_qty = quantity
    for i in range(0, second_num+1, interval):
        print("time left, i=" + str(i))
        if i == second_num:
            simulate_order(ticker, remain_qty)
            send_order(ticker, remain_qty, limit_price='sell',  type=type)
            # send_order(ticker, remain_qty, 'sell', type=type)
        else:
            simulate_order(ticker, min_size)
            send_order(ticker, min_size, limit_price='sell', type=type)
            # send_order(ticker, min_size, 'sell')
            remain_qty = remain_qty - min_size
        if remain_qty > 0:
            time.sleep(interval)
        else:
            return None

'''
optimize for execution parameter, for more efficient and cost control

@TODO   : need market data for optimization
'''
def optimizer(total_seconds, interval, total_shares, minimum_shares):
    exec_times = int(total_seconds/interval)
    shares_times = int(total_shares, minimum_shares)
    if exec_times > 2 * shares_times:
        return

def run_script():
    is_done = False
    print('Press Ctrl-C to quit.')
    try:
        while not is_done:
            stock = '600999'
            minimum_size = 10000
            type = "margin"
            # twap(stock, 1000, start_time="09:43:00", end_time="09:44:00", interval=5, min_size=minimum_size)
            twap(stock, 1300000, duration=60, interval=25, min_size=minimum_size, type=type)
            is_done = True
    except KeyboardInterrupt:
        print('\n')
        exit(0)


if __name__ == '__main__':
    # stock = '601688'
    # minimum_size = 10000
    # send_order(stock, minimum_size)
    # send_order(stock, minimum_size, 19.2)
    # twap(stock, 1000000, 0.5, interval=5, min_size=minimum_size)
    # twap(stock, 1000000, start_time="01:04:00", end_time="01:05:00", interval=5, min_size=minimum_size)
    run_script()