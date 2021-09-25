# -*- coding:utf-8 -*-

import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
# 列表里面内嵌列表的数据
print(a)
# 插入的时候并展开原来的内嵌
b = np.insert(a, 3, [11, 12])

print(b)
# 表示在第三行处插入
print("表示在第三行处插入")
c = np.insert(a, 2, [11, 12], axis=0)

print(c)

#
print("表示在第三列插入11")
d = np.insert(a, 2, 11, axis=1)

print(d)
# 表示删除第三个元素
# 没有axis 参数多重数组会被展开
e = np.delete(d, 2)
print(e)

#
print("表示删除第二列")
print(np.delete(d, 1, axis=1))
