# -*- coding:utf-8 -*-

import numpy as np

data_001 = np.arange(16)

print(data_001)

data_002 = data_001.reshape(4, 4)

print(data_002)

print(data_002.T)

# concatenate 连接两个形状相同的数组

data_003 = np.concatenate((data_002, data_002.T))
print("*" * 20)

print(data_003)
# 将数组分割为子数组
data_004 = np.split(data_001, 4)

print(data_004)

# 垂直分割
data_005 = np.hsplit(data_003, 4)
print("="*20)
print(data_005)
