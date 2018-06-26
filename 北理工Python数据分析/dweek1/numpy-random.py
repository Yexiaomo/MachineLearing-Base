#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def test1():
    ta1 = np.random.rand(3, 4, 5)
    tb1 = np.random.randn(3, 4, 5)
    tc1 = np.random.randint(100, 200, (3, 4))
    # td1 = np.random.seed(10)

    # print('ta1\n', ta1)
    # print('tb1\n', tb1)
    print('tc1\n', tc1)
def test2():
    a = np.random.randint(100, 200, (3,4))

    print('原始a\n', a)
    for i in range(5):
        np.random.shuffle(a)
        # 发现a在不断改变
        print("第{0}次shuffle后的a\n{1}".format(i+1 ,a))

    print('原始a\n', a)
    for i in range(5):
        np.random.permutation(a)
        # 发现a在没有改变
        print("第{0}次permutation后的a\n{1}".format(i+1 ,a))

def test3():
    tb3 = np.random.randint(100, 200, (8,))
    print('原始tb3\n', tb3)
    for i in range(5):
        tc3 = np.random.choice(tb3, (3,2), p=tb3/np.sum(tb3))
        print('tb3 choice后的tc3\n', tc3)
test3()