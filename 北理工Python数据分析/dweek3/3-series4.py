#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

b = pd.Series([9,8,7,6], ['a', 'b', 'c', 'd'])
print('b:\n', b)
print('b.index:\n', b.index)
print('b.value:\n', b.values)

# 索引和切片
print('b[3]:', b[3])
print('b[:3]:\n', b[:3])

print('b.median():',b.median())
print('b[b<b.median()]:\n', b[b<b.median()])
print('np.exp(b):\n', np.exp(b))

print("b['b']:", b['b'])
print("('c' in b):", 'c' in b) # 判断 'c' 是否是 b 中的索引
print("(0 in b):", 0 in b)
print("b.get('f', 100):", b.get('f', 100)) # 提取索引为'f'的值,如不存在则返回参数值 100(原则上返回 NaN, 但指定了参数)

# Series 对齐
b2 = pd.Series([1,2,3], ['c', 'd', 'e'])
print('b2:\n', b2)
print('b:\n', b)
print('b2+b =\n', b2+b)

# Series类型的name属性
# Series对象及索引都有一个名字,存储在属性.name中
print('b.name:',b.name)
print('b.index.name:',b.index.name)
b.name = "Series对象b"
b.index.name = "Series对象b索引"
print('b.name:',b.name)
print('b.index.name:',b.index.name)