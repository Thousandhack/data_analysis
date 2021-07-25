import numpy as np

# 1.导入并查看NumPy版本
print(np.__version__)

# 2.创建十个全为0的一维数组
print(np.zeros(10))
for value in np.zeros(10, dtype='float'):
    print(float(value), type(value))


# 3.创建10个全为0的一维数据并修改数据类型为整数
for value in np.zeros(10, dtype='int'):
    print(value, type(value))
