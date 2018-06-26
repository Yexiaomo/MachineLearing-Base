#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 基本统计分析函数
import pandas as pd
import numpy as np

a = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
print('a:\n{0}'.format(a))
print('a.decribe():\n{0}'.format(a.describe()))
print('type(a.describe()):\n{0}'.format(type(a.describe())))
print("a.describe()['count']:\n{0}".format(a.describe()['count']))

b = pd.DataFrame(np.arange(20).reshape(4,5), index=['c', 'a', 'b', 'd'])
print("\nb:\n{0}".format(b))
print('b.decribe():\n{0}'.format(b.describe()))
print('type(b.describe()):\n{0}'.format(type(b.describe())))
print("b.describe().ix['count']:\n{0}".format(b.describe().ix['count']))
print('b.describe()[2]:\n{0}'.format(b.describe()[2]))
