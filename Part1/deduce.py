# 一维数组
print([i * 2 for i in range(10)])
print([i * i for i in range(10)])
print([i * i for i in range(10) if (i % 3) == 0])
print([(x, y) for x in range(3) for y in range(3)])
print('')

# 二维数组
a = [[3] * (i + 1) for i in range(3)]
a[1][0] = 1
print(a)  # [[3], [1, 3], [3, 3, 3]]
print('')

# 乘法的问题
a = [[1, 2, 3]] * 3
a[1][1] = 100
print(a)  # [[1, 100, 3], [1, 100, 3], [1, 100, 3]]:因为复制二维数组时，传的是引用，所以只修改一个其他的也会变。
print('')

# 解决方法
a = [[1, 2, 3] for i in range(3)]
a[1][1] = 100
print(a)  # [[1, 2, 3], [1, 100, 3], [1, 2, 3]]
