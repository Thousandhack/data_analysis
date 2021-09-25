# -*- coding:utf-8 -*-

import numpy as np

data_001 = np.ones(5, dtype=float)

print(data_001)

# linspace 生成一个等差数列
data_002 = np.linspace(0, 5, 6)
print(data_002)

data_002 = np.linspace(0, 5, 6, endpoint=False)  # 表示最后一个参数不包含终止点
print(data_002)

# logspace 生成一个等比数列
data_003 = np.logspace(1, 10, 10, base=2)
print(data_003)

print(data_003[2])