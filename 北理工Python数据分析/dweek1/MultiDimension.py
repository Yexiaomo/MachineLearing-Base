#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

def test1():
    a = np.arange(100).reshape(5,10,2)
    a.tofile('multiDi.dat', sep=',', format='%d')

def test2():
    # .fromfile() 需要知道存入文件时数组的维度和元素类型
    # .tofile()和.fromfile()需要配合使用
    # 可以通过元数据文件来存储额外信息
    c = np.fromfile('multiDi.dat', dtype=np.int, sep=',').reshape(5,10,2)

    print('c\n', c)

def test3():
    at3 = np.arange(100).reshape(5,10,2)
    np.save('at3.npy', at3)
    bt3 = np.load('at3.npy')
    print('bt3\n', bt3)
        
test3()