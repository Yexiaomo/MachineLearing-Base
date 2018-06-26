#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def test1():
    ta1 = np.arange(15).reshape(3,5)
    print('ta1\n', ta1)
    print('np.sum(ta1)\n', np.sum(ta1))
    print('np.mean(ta1)\n', np.mean(ta1))
    print('np.mean(ta1, axis=1)\n', np.mean(ta1, axis=1))
    print('np.mean(ta1, axis=0)\n', np.mean(ta1, axis=0))
    print('np.average(ta1, axis=0, weights=[10, 5, 1])\n', np.average(ta1, axis=0, weights=[10, 5, 1]))
    print('np.std(ta1)\n', np.std(ta1))
    print('np.var(ta1)\n', np.var(ta1))

test1()