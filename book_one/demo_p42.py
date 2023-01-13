import numpy as np

# 数组操作2

# 连接数组
a = np.array([[1, 2], [3, 4]])
print(a)

b = np.array([[5, 6], [7, 8]])
print(b)

print(np.concatenate((a, b)))

print(np.concatenate((a, b), axis=1))
# 分割数组
print("沿轴0堆叠两个数组：")
print(np.stack((a, b), 0))
print("沿轴1堆叠两个数组：")
print(np.stack((a, b), 1))
# np.hstack 是 np.stack的变体，通过水平堆叠来生成数组
print("水平堆叠：")
c = np.hstack((a, b))
print(c)
print("垂直堆叠：")
d = np.vstack((a, b))
print(d)

e = np.arange(12)
print("起始数组：")
f = np.split(e, 4)
print("将数组分成三个大小相等的位置分割：")
print(f)
print("将数组一维数组中表明的位置分割")
g = np.split(a, [4, 7])
print(g)
# 水平分割数组： np.hsplit
i = np.floor(100 * np.random.randn(3, 9))
print("初始数组：")
print(i)
print("拆分后的数组：")
j = np.hsplit(i, 3)
print(j)

# np.vsplit 沿垂直轴分割
m = np.arange(12).reshape(4, 3)
print("初始数组：")
print(m)
print("竖直分割：")
print(np.vsplit(m, 2))
