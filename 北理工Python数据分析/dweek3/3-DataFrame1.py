#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# 从二维ndarray对象创建
d = pd.DataFrame(np.arange(10).reshape(2,5))
print("d:\n{0}".format(d))
# 从一维ndarray对象字典创建
dt = {'one' : pd.Series([1,2,3], index=['a', 'b', 'c']), \
      'two': pd.Series([9,8,7,6], index=['a', 'b', 'c', 'd'])}
print("dt:\n", dt)

d = pd.DataFrame(dt)
print("d:\n{0}".format(d))
# 从列表类型的字典创建
dl = {'one':[1,2,3], \
      'two':[9,8,7]}
print("dl:\n{0}".format(dl))
d = pd.DataFrame(dl, index = ['a', 'b', 'c'])
print("d:\n{0}".format(d))

'''中文类型创建, 表格如下

| 城市 | 对比 | 同比 | 定基 |
---------------------------
| 北京 |101.5| 120.7| 121.4|
| 上海 |101.2| 127.3| 127.8|
| 广州 |101.3| 119.4| 120.0|
| 深圳 |102.0| 140.9| 145.5|
| 沈阳 |100.1| 101.4| 101.6|

'''
dl = {'城市':['北京', '上海', '广州', '深圳', '沈阳'], \
      '环比':['101.5', '101.2', '101.3', '102.0', '100.1'], \
      '同比':['120.7', '127.3', '119.4', '140.9', '101.4'], \
      '定基':['121.4', '127.8', '120.0', '145.5', '101.6]']}

d = pd.DataFrame(dl, index=['c1', 'c2', 'c3', 'c4', 'c5'])
# d.values 返回了一个ndarray类型的array
print("d:\n{0}\nd.values:\n{1}".format(d, d.values))

# 获得 一列
print("d['城市']:\n{0}".format(d['城市']))
# 获得 一行
print("d.ix['c2']:\n{0}".format(d.ix['c2']))
# 获得 某一个值
print("d['城市']['c2']:\n{0}".format(d['城市']['c2']))