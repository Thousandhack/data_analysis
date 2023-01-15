import numpy as np

# 数组重新形成新的数组

print("初始数组")
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
# 数组的形状
print(a.shape)

b = np.resize(a, (3, 2))  # 返回指定形状的数组
print(b)
# b 数组的形状
print(b.shape)

c = np.resize(a, (3, 3))  # 返回指定形状的数组
print(c)
# 修改原来数组的大小
print(c.shape)
