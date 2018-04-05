import numpy as np
from pandas import Series, DataFrame

# 用字典生成DataFrame，key为列的名字
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
print(DataFrame(data))
'''
   pop   state  year
0  1.5    Ohio  2000
1  1.7    Ohio  2001
2  3.6    Ohio  2002
3  2.4  Nevada  2001
4  2.9  Nevada  2002
'''
print(DataFrame(data, columns=['year', 'state', 'pop']))  # 指定列顺序
'''
   year   state  pop
0  2000    Ohio  1.5
1  2001    Ohio  1.7
2  2002    Ohio  3.6
3  2001  Nevada  2.4
4  2002  Nevada  2.9
'''
print('')

# 指定索引，在列中指定不存在的列，默认数据用NaN
frame2 = DataFrame(data,
                   columns=['year', 'state', 'pop', 'debt'],
                   index=['one', 'two', 'three', 'four', 'five'])
print(frame2)
'''
       year   state  pop debt
one    2000    Ohio  1.5  NaN
two    2001    Ohio  1.7  NaN
three  2002    Ohio  3.6  NaN
four   2001  Nevada  2.4  NaN
five   2002  Nevada  2.9  NaN
'''
print(frame2['state'])
'''
one        Ohio
two        Ohio
three      Ohio
four     Nevada
five     Nevada
Name: state, dtype: object
'''
print(frame2.year)
'''
one      2000
two      2001
three    2002
four     2001
five     2002
Name: year, dtype: int64
'''
print(frame2.ix['three'])
'''
year     2002
state    Ohio
pop       3.6
debt      NaN
Name: three, dtype: object
'''
frame2['debt'] = 16.5
print(frame2)
'''
       year   state  pop  debt
one    2000    Ohio  1.5  16.5
two    2001    Ohio  1.7  16.5
three  2002    Ohio  3.6  16.5
four   2001  Nevada  2.4  16.5
five   2002  Nevada  2.9  16.5
'''
frame2.debt = np.arange(5)
print(frame2)
'''
       year   state  pop  debt
one    2000    Ohio  1.5     0
two    2001    Ohio  1.7     1
three  2002    Ohio  3.6     2
four   2001  Nevada  2.4     3
five   2002  Nevada  2.9     4
'''
print('')

# 用Series指定要修改的索引及其对应的值，没有指定的默认数据用NaN
val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print(frame2)
print('')
'''
       year   state  pop  debt
one    2000    Ohio  1.5   NaN
two    2001    Ohio  1.7  -1.2
three  2002    Ohio  3.6   NaN
four   2001  Nevada  2.4  -1.5
five   2002  Nevada  2.9  -1.7
'''

# 赋值给新列
frame2['eastern'] = (frame2.state == 'Ohio')  # 如果state等于Ohio为True
print(frame2)
'''
       year   state  pop  debt  eastern
one    2000    Ohio  1.5   NaN     True
two    2001    Ohio  1.7  -1.2     True
three  2002    Ohio  3.6   NaN     True
four   2001  Nevada  2.4  -1.5    False
five   2002  Nevada  2.9  -1.7    False
'''
print(frame2.columns)  # Index(['year', 'state', 'pop', 'debt', 'eastern'], dtype='object')
print('')

# DataFrame转置
pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = DataFrame(pop)
print(frame3)
'''
      Nevada  Ohio
2000     NaN   1.5
2001     2.4   1.7
2002     2.9   3.6
'''
print(frame3.T)
'''
        2000  2001  2002
Nevada   NaN   2.4   2.9
Ohio     1.5   1.7   3.6
'''
print('')

# 指定索引顺序，以及使用切片初始化数据
print(DataFrame(pop, index=[2001, 2002, 2003]))
'''
      Nevada  Ohio
2001     2.4   1.7
2002     2.9   3.6
2003     NaN   NaN
'''
pdata = {'Ohio': frame3['Ohio'][:-1], 'Nevada': frame3['Nevada'][:2]}  # 前者是取到倒数第一个，后者是取到第二个，在总长等于3的情况下相等
print(DataFrame(pdata))
'''
      Nevada  Ohio
2000     NaN   1.5
2001     2.4   1.7
2002     2.9   NaN
'''
print('')

# 指定索引和列的名称,貌似没什么用，只是print的时候会多个表头。
frame3.index.name = 'year'
frame3.columns.name = 'state'
print(frame3)
'''
state  Nevada  Ohio
year               
2000      NaN   1.5
2001      2.4   1.7
2002      2.9   3.6
'''
print(frame3.values)
'''
[[nan 1.5]
 [2.4 1.7]
 [2.9 3.6]]
'''
print(frame2.values)
'''
[[2000 'Ohio' 1.5 nan True]
 [2001 'Ohio' 1.7 -1.2 True]
 [2002 'Ohio' 3.6 nan True]
 [2001 'Nevada' 2.4 -1.5 False]
 [2002 'Nevada' 2.9 -1.7 False]]
'''
