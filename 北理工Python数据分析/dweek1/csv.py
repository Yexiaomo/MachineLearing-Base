#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
# np.savetxt() 只是常用于存储为CSV文件

def test1():
    a = np.arange(100).reshape((5,20))
    np.savetxt('testCSV.csv', a, fmt='%d', delimiter=',')
def test2():
    test1()
    b = np.loadtxt('testCSV.csv', delimiter=',')
    c = np.loadtxt('testCSV.csv', dtype=np.int, delimiter=',')
    print('b\n', b)
    print('c\n', c)

test2()