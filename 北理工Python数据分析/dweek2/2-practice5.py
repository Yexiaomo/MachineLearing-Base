#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 显示中文 rcParams

import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# rcParams 是matplotlib用来改变全局字体的资源库
def test1():
    matplotlib.rcParams['font.family'] = 'SimHei'
    plt.plot([3,1,4,2,5])
    plt.ylabel('纵轴(值)')
    plt.show()

# 绘制正弦波
def test2():
    matplotlib.rcParams['font.family'] = 'STSong'
    matplotlib.rcParams['font.size'] = 20

    a = np.arange(0.0, 5.0, 0.02)
    plt.xlabel('横轴: 时间')
    plt.ylabel('纵轴: 振幅')

    plt.plot(a, np.cos(2*np.pi*a), 'r--')
    plt.show()

test2()