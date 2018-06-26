#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

# pandas索引类型常用方法
dl = {'城市':['北京', '上海', '广州', '深圳', '沈阳'], \
      '环比':['101.5', '101.2', '101.3', '102.0', '100.1'], \
      '同比':['120.7', '127.3', '119.4', '140.9', '101.4'], \
      '定基':['121.4', '127.8', '120.0', '145.5', '101.6']}

d = pd.DataFrame(dl, index=['c1', 'c2', 'c3', 'c4', 'c5'])
nc = d.columns.delete(2)
ni = d.index.insert(5, 'c0')
print("d:\n{0}".format(d))
print("nc:\n{0}".format(nc))
print("ni:\n{0}".format(ni))

nd = d.reindex(index=ni, columns=nc, method='ffill')
print("nd:\n{0}".format(nd))

a = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
print("a:\n{0}".format(a))
ad =a.drop(['b', 'c'])
print("ad:\n{0}".format(ad))
nd_drop = nd.drop('c0')
print("nd_drop:\n{0}".format(nd_drop))
nd_drop2 = nd_drop.drop('同比', axis=1)
print("nd_drop2:\n{0}".format(nd_drop2))