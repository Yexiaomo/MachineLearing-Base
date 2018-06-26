#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

d = pd.Series(range(20))

print('d:\n', d)
# 计算前N项的和
print('d.cumsum():\n', d.cumsum())