import numpy as np

# 数组元素的添加和删除
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print("向a添加元素")
print(np.append(a, [7, 8, 9]))
print("沿轴0添加元素")
print(np.append(a, [[7, 8, 9]], axis=0))

print("沿轴1添加元素")
print(np.append(a, [[7, 8, 9], [2, 4, 6]], axis=1))

# 数组的插入
b = np.array([[1, 2], [3, 4], [5, 6]])
print("数组b")
print(b)
print("未传axis 参数， 在插入之前输入数组b会被展开")
print(np.insert(b, 3, [11, 12]))

print("沿轴0插入元素")
print(np.insert(b, 1, [8], axis=0))
print("沿轴1插入元素")
print(np.insert(b, 1, 11, axis=1))

# 删除元素

c = np.arange(15).reshape(3, 5)
print("数组c")
print(c)
print("未传axis 参数， 在插入之前输入数组d会被展开")
print(np.delete(c, 8))
print("删除第二列")
print(np.delete(c, 1, axis=1))

print("删除第二行")
print(np.delete(c, 1, axis=0))

# 去重
d = np.array([1, 2, 3, 45, 3, 3, 2, 3, 4, 3, 4, 325, 56, 743, 32])
print("数组d")
print(d)
print("去重")
print(np.unique(d))
print("去重后并返回去重后元素的索引")
print(np.unique(d, return_index=True))

print("返回去重的元素和数量个数")
print(np.unique(d, return_counts=True))
