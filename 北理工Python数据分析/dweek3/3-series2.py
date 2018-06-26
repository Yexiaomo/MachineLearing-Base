#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

d1 = pd.Series([9, 8, 7, 6])
print('d1:\n', d1)

d2 = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
print('d2:\n', d2)