import numpy as np

# 等差数列    开始值    结束值 样本数量 endpoint 表示是否包含结束值
# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None,axis=0)

a = np.linspace(0, 5, 6)
print(a)

b = np.linspace(0, 5, 3)
print(b)
# 不包含的话，就相当于会多分出一份等差数据，然后去掉最后一个
c = np.linspace(0, 5, 3, endpoint=False)
print(c)
