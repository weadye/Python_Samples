import numpy as np

# 使用普通一维数组生成NumPy一维数组
data = [6, 7.5, 8, 0, 1]
arr = np.array(data)
print(arr)  # [6.  7.5 8.  0.  1. ]
print(type(arr))  # <class 'numpy.ndarray'>

# 使用普通二维数组生成NumPy二维数组
data = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr = np.array(data)
print(arr)
'''
[[1 2 3 4]
 [5 6 7 8]]
'''
print(arr.shape)  # 维度：(2, 4)，类型是tuple
print(arr[0, 1])  # 2
print('')

# 使用zeros/empty
print(np.zeros(10))  # 生成包含10个0的一维数组
print(np.zeros((3, 6)))  # 生成3*6的二维数组
'''
[[0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]]
'''
print(np.zeros((2, 3, 2)))  # 生成2*3*2的三维数组
'''
[[[0. 0.]
  [0. 0.]
  [0. 0.]]

 [[0. 0.]
  [0. 0.]
  [0. 0.]]]
'''
print(np.ones((2, 3)))  # 生成2*3的全由1组成的矩阵
'''
[[1. 1. 1.]
 [1. 1. 1.]]
'''
print(np.full((2, 3), 6))  # 生成2*3的全由6组成的矩阵
'''
[[6 6 6]
 [6 6 6]]
'''
print(np.eye(5))  # 生成单位矩阵
'''
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
'''
print(np.random.random((3, 2)))  # 生成3*2的由0-1中的随机数组成的矩阵
'''
[[0.61204847 0.87704669]
 [0.53194939 0.89201115]
 [0.05492793 0.35919411]]
'''

print(np.empty((2, 3, 4)))  # 生成一个2*3*4的未初始化的矩阵，内容随机，但是生成速度会比zeros快
'''
[[[6.23042070e-307 4.67296746e-307 1.69121096e-306 7.56593696e-307]
  [1.42413555e-306 1.78019082e-306 1.37959740e-306 6.23057349e-307]
  [1.02360935e-306 1.69120416e-306 1.78022342e-306 6.23058028e-307]]

 [[1.06811422e-306 1.22383391e-307 8.01097889e-307 1.78020169e-306]
  [7.56601165e-307 1.02359984e-306 1.33510679e-306 2.22522597e-306]
  [1.78019761e-306 1.78019761e-306 1.20160711e-306 2.56765117e-312]]]
'''
g = np.arange(15)  # 生成一个15维的数组
print(g)  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
print(g.shape)  # (15,)
print('')

arr = np.array([1, 2, 3])  # 生成数组时可以指定数据类型，如果不指定，numpy会自动匹配合适的类型
print(arr.dtype)  # int32
print(arr)  # [1 2 3]

arr = np.array([1, 2, 3], dtype=np.float64)  # 生成数组时可以指定数据类型为float64
print(arr, arr.dtype)  # [1. 2. 3.] float64

int_arr = np.array([1, 2, 3, 4, 5])
print(int_arr, int_arr.dtype)  # [1 2 3 4 5] int32

float_arr = int_arr.astype(np.float)  # 将数组的dtype由int转为float
print(float_arr, float_arr.dtype)  # [1. 2. 3. 4. 5.] float64

str_arr = np.array(['1.24', '2.2', '5.8'], dtype=np.string_)  # 创建一个string数组
print(str_arr, str_arr.dtype)  # [b'1.24' b'2.2' b'5.8'] |S4

float_arr = str_arr.astype(np.float)
print(float_arr, float_arr.dtype)  # [1.24 2.2  5.8 ] float64

str_arr = np.array(['1.24', '2.2', '5.8', 'error'], dtype=np.string_)  # string数组转成float失败则会抛出异常
# ! float_arr = str_arr.astype(np.float)
# ValueError: could not convert string to float: 'error'
