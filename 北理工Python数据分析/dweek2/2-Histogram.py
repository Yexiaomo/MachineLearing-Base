#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 直方图

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
mu, sigma = 100, 20 # 均值, 标准差
a = np.random.normal(mu, sigma, size=100)

plt.subplot(2,1,1)
plt.hist(a, 20, normed=1, histtype='stepfilled', facecolor='b', alpha=0.75)
plt.title('Histogram')

# 参数bins的不同可对比图像观察不同
plt.subplot(2,1,2)
plt.hist(a, 40, normed=1, histtype='stepfilled', facecolor='b', alpha=0.75)
plt.title('Histogram')
plt.show()