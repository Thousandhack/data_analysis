# -*- coding:utf-8 -*-

import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])

print(a, type(a))
# [1 2 3 4 5 6] <class 'numpy.ndarray'>
print(a.ndim)
# 即轴的数量或者维度数量

data_001 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
]

b = np.array(data_001)

print(b)
#  [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]

print(b.ndim)   # 即轴的数量或者维度数量
print(b.dtype)  # 打印数据类型
print(b.shape)  # n 行 m 列
print(b.size)   # 数组元素的总个数
print(b.flags)
"""
对象的内存信息:
  C_CONTIGUOUS : True
  F_CONTIGUOUS : False
  OWNDATA : True
  WRITEABLE : True
  ALIGNED : True
  WRITEBACKIFCOPY : False
  UPDATEIFCOPY : False
"""
