#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 累计统计分析函数
import pandas as pd
import numpy as np
b = pd.DataFrame(np.arange(20).reshape(4,5), index=['c', 'a', 'b', 'd'])
print('b:\n{0}'.format(b))
print('b.cumsum():\n{0}'.format(b.cumsum()))
print('b.cumprod():\n{0}'.format(b.cumprod()))
print('b.cummin():\n{0}'.format(b.cummin()))
print('b.cummax():\n{0}'.format(b.cummax()))

print('\n\nb:\n{0}'.format(b))
print('b.rolling(2):\n{0}'.format(b.rolling(2).sum()))
print('b.rolling(3):\n{0}'.format(b.rolling(3).sum()))

