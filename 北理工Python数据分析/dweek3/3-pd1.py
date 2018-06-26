#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pandas索引类型常用方法
import pandas as pd

dl = {'城市':['北京', '上海', '广州', '深圳', '沈阳'], \
      '环比':['101.5', '101.2', '101.3', '102.0', '100.1'], \
      '同比':['120.7', '127.3', '119.4', '140.9', '101.4'], \
      '定基':['121.4', '127.8', '120.0', '145.5', '101.6']}

d = pd.DataFrame(dl, index=['c1', 'c2', 'c3', 'c4', 'c5'])
print('d:\n{0}'.format(d))
d = d.reindex(index=['c5', 'c4', 'c3', 'c2', 'c1'])
print('d:\n{0}'.format(d))
d = d.reindex(columns=['城市', '同比', '环比', '定基'])
print('d:\n{0}'.format(d))

newc = d.columns.insert(4, '新增')
newi = d.index.insert(0, 'c6')
newd = d.reindex(columns=newc, fill_value=200)
print('newc:\n{0}'.format(newc))
print('newi:\n{0}'.format(newi))
print('newd:\n{0}'.format(newd))
print("newd['城市'],['c5']:",newd['新增']['c5'])