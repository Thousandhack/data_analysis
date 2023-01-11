import numpy as np

# 等比数列
# 起始值为 base**start
# 结束值为 base**stop
# 是否包括结束值 endpoint=True

# logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0):
a = np.logspace(1, 10, 10, base=2)
print(a)
