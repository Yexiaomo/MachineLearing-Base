#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PIL指的是 pillow 库
from PIL import Image
import numpy as np

def test1():
    # 1.打开图像
    a = np.array(Image.open('python.jpg'))
    print(a.shape, a.dtype)

    #2.改变图像的rgb值 计算rgb的补值
    b = [255, 255, 255] - a 

    #3.保存图像
    im = Image.fromarray(b.astype('uint8'))
    im.save('changePythonImg1.jpg')

def test2():
    # convert('L')将一个彩色图片转化为灰色图片
    a = np.array(Image.open('python.jpg').convert('L'))
    c = 255 - a
    im = Image.fromarray(c.astype('uint8'))
    im.save('changePythonImg2.jpg')

def test3():
    a = np.array(Image.open('python.jpg').convert('L'))
    d = (100/255)*a + 150
    im = Image.fromarray(d.astype('uint8'))
    im.save('changePythonImg3.jpg')

def test4():
    a = np.array(Image.open('python.jpg').convert('L'))
    e = 255 * (a/255)**2 #像素的平方
    im = Image.fromarray(e.astype('uint8'))
    im.save('changePythonImg4.jpg')

test4()