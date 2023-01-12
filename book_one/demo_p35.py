import numpy as np

# 索引
# 随机生成6个数据
arr_list = np.random.randn(6)
print(arr_list)

print(arr_list[3])

print(arr_list[-2])
# 左闭右开 元素1到元素3
print(arr_list[1:3])

# 元素索引1 和 索引4 的值，形成新的array
print(arr_list[[1, 4]])

# 切片
print("切片")
print(arr_list[0:5:2])

d = np.random.randn(16).reshape(4, 4)
print("二维数组d:\n{}".format(d))
d1 = d[0, :]
print("数组第一行元素：{}".format(d1))

d2 = d[:, 0]
print("数组的第一列元素：{}".format(d2))

# 第2行至第3行 以及 第2列至第3列
print("第2行至第3行 以及 第2列至第3列")
print(d[1:3, 1:3])
# 行的索引1和2的元素  以及 第2列至第3列
print(d[[1, 2], 1:3])
