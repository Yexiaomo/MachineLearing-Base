#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 极坐标图
import numpy as np
import matplotlib.pyplot as plt

N = 20
theta = np.linspace(0.0, 2*np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)

ax = plt.subplot(111, projection='polar')
# 这里的 .bar() 函数的第一个参数颜色区域从哪开始, 中心点向边缘绘制的长度, 区域的面积(角度面积范围)
bars = ax.bar(theta, radii, width=width, bottom=0.0)
for r,bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r/10.))
    bar.set_alpha(0.5)
plt.show()