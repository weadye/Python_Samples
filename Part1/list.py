# 初始化列表
li = [1, 2, 3, 'abc', 4.5, [2, 3, 4], {1: 'one'}]  # list
tp = (1, 2, 3)  # tuple： 不可写，其他操作同list
# 获取长度
print(len(li))  # 7
print('')

# 根据索引读写
print(li[0])  # 1
print(li[3])  # abc
print(li[-1])  # {1: 'one'}
print('')

# 添加元素
li = [1, 2, 3]
li.append('a')
li.append('b')
print(li)  # [1, 2, 3, 'a', 'b']
li.append([4, 5, 6])
print(li)  # [1, 2, 3, 'a', 'b', [4, 5, 6]]
li.extend([4, 5, 6])
print(li)  # [1, 2, 3, 'a', 'b', [4, 5, 6], 4, 5, 6]
print('')

# 删除
li = [1, 2, 3, 4, 5]
li.pop()
print(li)  # [1, 2, 3, 4]
del (li[0])
del (li[1])
print(li)  # [2, 4]
print('')

# 列表是否为空
li = []
if not li:
    print('Empty')  # Empty
else:
    print('Not Empty')
li.append(1)
if len(li) == 0:
    print('Empty')
else:
    print('Not Empty')  # Not Empty
print('')

# 字符串： 字符串也可以用索引来访问，可以当做是一个数组（ps：字符串是不可写的！）
s = 'abcdefg'
li = list(s)
li[4] = 'E'
print(s)  # abcdefg
s = ''.join(li)
print(s)  # abcdEfg
print('')

# 遍历
li = [1, 2, 3]
for i in li:
    print(i)  # 1 2 3
for i in range(len(li)):
    print(li[i])  # 1 2 3
for i in range(len(li) - 1, -1, -1):
    print(li[i])  # 3 2 1
print(li[-1])  # 3
