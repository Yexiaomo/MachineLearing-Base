#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 相关性分析函数
## 房价增幅与M2增幅的相关性
import pandas as pd

hprice = pd.Series([3.04, 22.93, 12.75, 22.6, 12.33], \
                    index=["2008", "2009", "2010", "2011", "2012"])
m2 = pd.Series([8.18, 18.38, 9.13, 7.82, 6.69], \
                index=["2008", "2009", "2010", "2011", "2012"])
print("hprice.corr(m2):", hprice.corr(m2))