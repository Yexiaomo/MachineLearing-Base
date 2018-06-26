#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
#当参数只有一个维列表参数时,这个参数就被y轴,此时x轴就是索引
plt.plot([3,1,4,5,2])
#y轴标签
plt.ylabel('Garde')
#如果你想保存结果为图片(默认png格式)
#dpi越大图像质量越大,600就已经很高
plt.savefig('2practice1', dpi=600)
#显示结果
plt.show()