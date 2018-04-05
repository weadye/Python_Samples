import numpy as np
from numpy import nan as NA
import pandas as pd
from pandas import Series, DataFrame, Index

#填充0
df = DataFrame(np.random.randn(7,3))
df.ix[:4,1] = NA
df.ix[:2,2] = NA
print(df.fillna(0))
'''
          0         1         2
0 -0.837172  0.000000  0.000000
1 -0.243165  0.000000  0.000000
2  1.082605  0.000000  0.000000
3 -1.257098  0.000000 -1.925399
4  0.202267  0.000000 -0.671994
5 -1.460086 -0.297704  0.450831
6  0.374312 -0.119064  0.473813
'''
df = DataFrame(np.random.randn(7,3))
df.ix[:4,1] = NA
df.ix[:2,2] = NA
print(df.fillna(0,inplace = True)) #None  无返回值，直接改变df
print(df)
'''
          0         1         2
0  0.178941  0.000000  0.000000
1 -0.069864  0.000000  0.000000
2 -1.642611  0.000000  0.000000
3 -0.515321  0.000000 -0.633069
4 -1.024368  0.000000 -0.911951
5  0.624916  0.157028  0.466320
6  0.071537  0.803568 -0.922995
'''
# 不用行列填充不同的值
df.ix[:4,1] = NA
df.ix[:2,2] = NA
print(df.fillna({1:0.5,2:-1}))#第3列不存在
'''
          0         1         2
0  1.548890  0.500000 -1.000000
1 -0.226853  0.500000 -1.000000
2  0.732759  0.500000 -1.000000
3  1.636023  0.500000 -1.493595
4  0.735053  0.500000  0.009740
5 -0.423113 -0.710357 -0.586350
6  0.948998 -0.296592 -1.531374
'''
print('')

#不同的填充方式
df = DataFrame(np.random.randn(6,3))
df.ix[2:,1] = NA
df.ix[4:,2] = NA
print(df)
'''
          0         1         2
0 -0.538438  0.383027  0.843894
1 -0.533963  0.498426  0.692086
2  0.366839       NaN  0.760089
3 -0.700147       NaN  0.424176
4 -0.263781       NaN       NaN
5  0.903039       NaN       NaN
'''
print(df.fillna(method = 'ffill'))
'''
          0         1         2
0 -0.538438  0.383027  0.843894
1 -0.533963  0.498426  0.692086
2  0.366839  0.498426  0.760089
3 -0.700147  0.498426  0.424176
4 -0.263781  0.498426  0.424176
5  0.903039  0.498426  0.424176
'''
print(df.fillna(method = 'ffill', limit = 2))
'''
          0         1         2
0 -0.538438  0.383027  0.843894
1 -0.533963  0.498426  0.692086
2  0.366839  0.498426  0.760089
3 -0.700147  0.498426  0.424176
4 -0.263781       NaN  0.424176
5  0.903039       NaN  0.424176
'''
print('')

#用统计数据填充
data = Series([1.,NA,3.5,NA,7])
print(data.fillna(data.mean()))
'''
0    1.000000
1    3.833333
2    3.500000
3    3.833333
4    7.000000
dtype: float64
'''