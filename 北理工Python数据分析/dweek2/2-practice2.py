#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

#plt.plot(x,y) 当有两个以上的参数时,按照x轴和y轴顺序绘制数据点
plt.plot([0,2,4,6,8],[3,1,4,5,2])
plt.ylabel("Garde")
# plt.axis设定横纵坐标尺度
# 有四个参数依次为: x轴起始值,x轴结束值,y轴起始值,y轴结束值,
plt.axis([-1,10,0,6])
plt.show()