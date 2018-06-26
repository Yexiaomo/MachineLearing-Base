#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
# 从标量值创建
s = pd.Series(25, index=['a', 'b', 'c']) # 不能省略 index参数
print('s:\n', s)

# 从字典类型创建
d = pd.Series({'a':9, 'b':8, 'c':7})
print('d:\n', d)
d2 = pd.Series({'a':9, 'b':8, 'c':7}, index=['c', 'a', 'b', 'd'])
print('d2:\n', d2) # 打印结果可以发现索引从字典中进行选择; 若索引没有对应的值,则打印为 NaN

# 从ndarray类型创建

n = pd.Series(np.arange(5))
print('n:\n', n)

m = pd.Series(np.arange(5), index=np.arange(9,4,-1))
print('m\n',m)