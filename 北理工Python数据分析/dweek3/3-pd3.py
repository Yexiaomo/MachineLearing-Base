#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 数据排序
import pandas as pd
import numpy as np

b = pd.DataFrame(np.arange(20).reshape(4,5), index=['c', 'a', 'd', 'b'])
print("b:\n{0}".format(b))
b_sort = b.sort_index()
print("b_sort:\n{0}".format(b_sort))
b_sort2 = b.sort_index(ascending=False) # 降序,默认axis为0, 也就是竖轴
print("b_sort2:\n{0}".format(b_sort2))

print("b:\n{0}".format(b))
c = b.sort_values(2, ascending=False) # 按照第三列进行降序排列
print("c:\n{0}".format(c))
c2 = c.sort_values('a', axis=1, ascending=False) # 按照第三列进行降序排列
print("c2:\n{0}".format(c2))

b2 = pd.DataFrame(np.arange(9).reshape(3,3), index=['a', 'b', 'c'])
print("b2:\n{0}".format(b2))
b3 = b + b2
print("b3:\n{0}".format(b3))

print("b3.sort_values(2, aseconding=True):\n{0}".format(b3.sort_values(2, ascending=True)))
print("b3.sort_values(2, aseconding=False):\n{0}".format(b3.sort_values(2, ascending=False)))