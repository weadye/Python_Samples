import numpy as np

arr1 = np.array([[1, 2], [3, 4]], dtype=np.float64)
arr2 = np.array([[5, 6], [7, 8]], dtype=np.float64)
# 逐元素求和
print(arr1 + arr2)
'''
[[ 6.  8.]
 [10. 12.]]
'''
# 逐元素求差
print(arr1 - arr2)
'''
[[-4. -4.]
 [-4. -4.]]
'''
# 逐元素相乘，也可以使用np.multiply
print(arr1 * arr2)
'''
[[ 5. 12.]
 [21. 32.]]
'''
# 逐元素相除
print(arr1 / arr2)
'''
[[0.2        0.33333333]
 [0.42857143 0.5       ]]
'''
# 逐元素求平方根
print(np.sqrt(arr1))
'''
[[1.         1.41421356]
 [1.73205081 2.        ]]
'''
# 求矩阵乘积
print(np.dot(arr1, arr2))
'''
[[19. 22.]
 [43. 50.]]
'''
# 求矩阵转置 a[i,j], a[j,i] = a[j,i], a[i,j]
print(arr1.T)
'''
[[1. 3.]
 [2. 4.]]
'''
# reshape的用法
arr = np.arange(16).reshape(2, 2, 4)
print(arr, arr.shape)
'''
[[[ 0  1  2  3]
  [ 4  5  6  7]]

 [[ 8  9 10 11]
  [12 13 14 15]]] (2, 2, 4)
'''
# 高维数组的转置,详见：https://blog.csdn.net/Hearthougan/article/details/72626643?locationNum=7&fps=1
print(arr.transpose((0, 2, 1)))
'''
[[[ 0  4]
  [ 1  5]
  [ 2  6]
  [ 3  7]]

 [[ 8 12]
  [ 9 13]
  [10 14]
  [11 15]]]
'''
# 交换第1,2（实际上是2,3）维，实际功能和上一个例子是一样的
print(arr.swapaxes(1, 2))
'''
[[[ 0  4]
  [ 1  5]
  [ 2  6]
  [ 3  7]]

 [[ 8 12]
  [ 9 13]
  [10 14]
  [11 15]]]
'''
# 矩阵求和
arr = np.array([[1, 2], [3, 4]])
print(np.sum(arr))  # 10
print(np.sum(arr, axis=0))  # 按列求和 [4 6]
print(np.sum(arr, axis=1))  # 按行求和 [3 7]
# 矩阵求平均
print(np.mean(arr))  # 2.5
print(np.mean(arr, axis=0))  # 按列求平均 [2. 3.]
print(np.mean(arr, axis=1))  # 按行求平均 [1.5 3.5]
# 矩阵求累加
print(np.cumsum(arr))  # [ 1  3  6 10]
print(np.cumsum(arr, axis=0))  # 按列求累加
'''
[[1 2]
 [4 6]]
'''
print(np.cumsum(arr, axis=1))  # 按行求累加
'''
[[1 3]
 [3 7]]
'''
# 矩阵求累乘
print(np.cumprod(arr))  # [ 1  2  6 24]
print(np.cumprod(arr, axis=0))  # 按列求累乘
'''
[[1 2]
 [3 8]]
'''
print(np.cumprod(arr, axis=1))  # 按行求累乘
'''
[[ 1  2]
 [ 3 12]]
'''
# 一维数组的排序
arr = np.random.random(8) * 10
print(arr)  # [4.02458128 7.01557261 3.17693492 0.06348229 4.03283679 9.43823173 1.61291647 1.12743554]
arr.sort()
print(arr)  # [0.1350891  2.56079004 3.0013661  5.45693107 5.89316928 7.12877039 8.353495   9.01955238]
arr = np.random.random((2, 4)) * 10
print(arr)
'''
[[2.70822329 8.41332988 5.94898667 6.91240623]
 [0.71610329 8.60703313 7.8554127  7.76183729]]
'''
arr.sort(0)  # 按列排序
print(arr)
'''
[[0.71610329 8.41332988 5.94898667 6.91240623]
 [2.70822329 8.60703313 7.8554127  7.76183729]]
'''
arr.sort(1)  # 按行排序
print(arr)
'''
[[0.71610329 5.94898667 6.91240623 8.41332988]
 [2.70822329 7.76183729 7.8554127  8.60703313]]
'''
