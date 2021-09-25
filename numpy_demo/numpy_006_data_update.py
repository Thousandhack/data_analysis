# -*- coding:utf-8 -*-

import numpy as np

data_001 = np.array([[1, 2, 3], [4, 5, 6]])
print(data_001)
print("*" * 20)

data_002 = np.append(data_001, [7, 8, 9])
print(data_002)
print("*" * 20)

data_003 = np.append(data_001, [[7, 8, 9]], axis=0)
print(data_003)
print("*" * 20)
