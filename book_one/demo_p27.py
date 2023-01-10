import numpy as np

# 生成一个二维数组
# 数组中每个列表的个数需要相同
# ndarray 对象中的里面的元素的数据类型是需要相同的
array_demo = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]

ndarray = np.array(array_demo)

for list_demo in ndarray:
    print(list_demo, "list_demo")
    for b in list_demo:
        print(b)

print(type(ndarray))

print("ndim", ndarray.ndim)  # 表示数组是几维数组
print("dtype", ndarray.dtype)  # 表示数组中元素的数据类型
print("shape", ndarray.shape)  # 直接表示几行几列
print("size", ndarray.size)  # n*m 数组元素的总个数


