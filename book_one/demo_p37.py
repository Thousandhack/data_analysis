import numpy as np

# 数组操作


# 修改数组形状
a = np.arange(12)
print(a)

b = a.reshape(3, 4)
print(b)  # 将数据从一维数组修改为 3*4的数组

# 翻转数组 就相当于把整个数组对折翻转
# ndarray.T 和 np.transpose 功能相似
c = np.arange(20).reshape(5, 4)
print("原始数组:\n{}".format(c))

d = np.transpose(c)
print("修改后的数组：\n{}".format(d))

e = c.T
print("T修改后的数组:\n{}".format(e))

# 修改数组维度
# 就是将一维数组的数值加到 第一个数组上，对于元素相加
f = np.arange(9).reshape(3, 3)
print("f原始数组:\n{}".format(f))
g = np.arange(3)
print("g原始数组:\n{}".format(g))
h = f + g
print("广播运算后的数组:\n{}".format(h))

# 数组维度改变
a1 = np.arange(4).reshape(1, 4)

b1 = np.broadcast_to(a1, (4, 4))
print("修改前")
print(a1)
print("修改后")
print(b1)
