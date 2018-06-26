#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 饼状图
import matplotlib.pyplot as plt

labels = 'Forgs', 'Hogs', 'Dog', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)

# equal值 使xy方向尺寸相等
plt.axis('equal') # 使饼状图是一个正圆形,而不是椭圆形

plt.show()