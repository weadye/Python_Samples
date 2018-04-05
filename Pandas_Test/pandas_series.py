from pandas import Series

# 用数组生成Series
obj = Series([4, 7, -5, 3])
print(obj)
'''
0    4
1    7
2   -5
3    3
dtype: int64
'''
print(obj.values)  # [ 4  7 -5  3]
print(obj.index)  # RangeIndex(start=0, stop=4, step=1)
print('')

# 指定Series的index
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
'''
d    4
b    7
a   -5
c    3
dtype: int64
'''
print(obj2.index)  # Index(['d', 'b', 'a', 'c'], dtype='object')
print(obj2['a'])  # -5
obj2['d'] = 6
print(obj2[['c', 'a', 'd']])
'''
c    3
a   -5
d    6
dtype: int64
'''
print(obj2[obj2 > 0])  # 找出大于0的元素
'''
d    6
b    7
c    3
dtype: int64
'''
print('b' in obj2)  # True 判断索引是否存在
print('e' in obj2)  # False
print('')

# 使用字典生成Series
sdata = {'Ohio': 45000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
print(obj3)
'''
Ohio      45000
Oregon    16000
Texas     71000
Utah       5000
dtype: int64
'''

# 使用字典生成Series,并额外指定index，不匹配部分为NaN
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)
print(obj4)
'''
California        NaN
Ohio          45000.0
Oregon        16000.0
Texas         71000.0
dtype: float64
'''

# 也可以使用下标访问
print(obj4[0], obj4[3])  # nan 71000.0

# Series相加， 相同索引部分相加
print(obj3 + obj4)
'''
California         NaN
Ohio           90000.0
Oregon         32000.0
Texas         142000.0
Utah               NaN
dtype: float64
'''
