import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6]])
bool_index = arr > 2  # 找到大于2的元素
print(bool_index)
'''
[[False False]
 [ True  True]
 [ True  True]]
'''
print(arr[bool_index])  # [3 4 5 6]
print(arr[arr > 3])  # [4 5 6]

arr1 = np.array([1.1,1.2,1.3,1.4,1.5])
arr2 = np.array([2.1,2.2,2.3,2.4,2.5])
cond = np.array([True,True,False,True,False])
#True时，从arr1中取值，False时，从arr2中取值
print(np.where(cond,arr1,arr2))#[1.1 1.2 2.3 1.4 2.5]

arr = np.random.randn(4,4)
print(arr)
'''
[[-1.82590305 -0.21688933  1.08333726 -0.19684418]
 [-0.44354733 -1.0558117   0.58723758 -0.9128545 ]
 [-0.42749422 -0.40276047  1.13543222  1.11311112]
 [-0.12436263  0.7241693   0.55727687 -1.02974109]]
'''
print(np.where(arr>0,1,-1))
'''
[[-1 -1  1 -1]
 [-1 -1  1 -1]
 [-1 -1  1  1]
 [-1  1  1 -1]]
'''
print(np.where(arr>0,1,arr))
'''
[[-1.82590305 -0.21688933  1.         -0.19684418]
 [-0.44354733 -1.0558117   1.         -0.9128545 ]
 [-0.42749422 -0.40276047  1.          1.        ]
 [-0.12436263  1.          1.         -1.02974109]]
'''