#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def test1():
    a = np.array([[0,1,2,3,4],[9,8,7,6,5]])
    # a = np.array([[0,1,2,3,4],[9,8,7,6,5], (0.1, 0.2)])
    print('a.ndim :', a.ndim)
    print('a.shape :', a.shape)
    print('a.size :', a.size)
    print('a.dtype :', a.dtype)
    print('a.itemsize :', a.itemsize)

def test2():
    print('arange(10)', np.arange(10))
    print('ones((3,3))', np.ones((3,3)))
    print('zeros(3,3)', np.zeros((3,3), dtype=np.int32))
    print('full((3,3),3)', np.full((3,3),3))
    print('eye(3)', np.eye(3))
def test3():
    a = np.linspace(1,10,4)
    b = np.linspace(1,10,4, endpoint=False)
    print('linspace()', a) #默认数据类型为浮点型
    print('linspace()', b)
    print('concatenate()', np.concatenate((a,b)) )

def test4():
    # 一维数组的索引和切片
    a = np.array([9,8,7,6,5])
    print('a[2]', a[2])
    print('a[1:4:2]', a[1:4:2])
    # 多维数组的索引
    b = np.arange(24).reshape((2,3,4))
    print('b', b)
    print('b[1,2,3]', b[1,2,3])
    print('b[0,1,2]', b[0,1,2])
    print('b[-1,-2,-3]', b[-1,-2,-3])
    # 多维数组的切片
    print( 'b[:, 1, -3]\n',b[:, 1, -3] )
    print( 'b[:, 1:3, :]\n',b[:, 1:3, :] )
    print( 'b[:, :, ::2]\n',b[:, :, ::2] )

def test5():
    a = np.arange(24).reshape((2,3,4))
    print('a\n', a)
    # 计算a与元素平均值的商
    print('a.mean()', a.mean()) # mean() 返回的是数组的平均值
    a = a / a.mean()
    print('a\n', a)

def test6():
    a = np.arange(24).reshape((2,3,4))
    print('np.square(a)\n', np.square(a))
    a =  np.sqrt(a)
    print('np.square(a)\n', a)
    print('np.modf(a)\n', np.modf(a))



test6()