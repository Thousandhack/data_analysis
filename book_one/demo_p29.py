import numpy as np

a = np.arange(25, dtype=np.float_).reshape(5, 5)

b = np.array([1, 2, 3, 4, 5, 6])

print(a)
print("a 的属性")
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.itemsize)

print(b)
