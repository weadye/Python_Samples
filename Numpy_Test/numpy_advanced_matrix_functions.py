import numpy as np

arr = np.arange(15)

print(arr.shape)  # (15,)
print(arr.reshape(3, 5).shape)  # (3, 5)
# 在某一维用-1将会自动计算
print(arr.reshape(3, -1).shape)  # (3, 5)
# ps: reshape()并不会改变矩阵本身，所以要用 arr = arr.reshape(x,y)来改变arr本身

# 用另一矩阵的shape来定义某一矩阵的shape
arr1 = np.arange(15)
arr = arr.reshape(3, -1)
print(arr1.shape, arr1.reshape(arr.shape).shape)  # (15,) (3, 5)
# 高维数组可以用ravel来拉平
print(arr.ravel())  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
# ps: ravel()和reshape()一样，并不会改变矩阵本身，所以要用 arr = arr.ravel()来改变arr本身

# 矩阵连接
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
print(np.concatenate([arr1, arr2], axis=0))  # 按列堆叠
'''
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
'''
print(np.concatenate([arr1, arr2], axis=1))  # 按行堆叠
'''
[[ 1  2  3  7  8  9]
 [ 4  5  6 10 11 12]]
'''
print(np.vstack((arr1, arr2)))  # 纵向堆叠
'''
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
'''
print(np.hstack((arr1, arr2)))  # 横向堆叠
'''
[[ 1  2  3  7  8  9]
 [ 4  5  6 10 11 12]]
'''
