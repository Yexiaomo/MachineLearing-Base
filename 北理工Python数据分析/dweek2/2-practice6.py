#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 显示中文(不建议使用rcParams改变全局的字体)
# 仅仅在有中文输出的地方,增加一个属性: fontproperties

import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0.0, 5.0, 0.02)

plt.xlabel('横轴: 时间', fontproperties='SimHei', fontsize=20)
plt.ylabel('纵轴: 振幅', fontproperties='SimHei', fontsize=20)
plt.plot(a, np.cos(2*np.pi*a), 'r--')
plt.show()