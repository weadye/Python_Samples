import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tushare as ts

# 获取数据
s_pf = '600000'  # 浦发银行
s_gd = '601818'  # 光大银行
sdate = '2016-01-01'
edate = '2016-12-31'
df_pf = ts.get_h_data(s_pf, start=sdate, end=edate).sort_index(axis=0, ascending=True)
df_gd = ts.get_h_data(s_gd, start=sdate, end=edate).sort_index(axis=0, ascending=True)
df = pd.concat([df_pf.close, df_gd.close], axis=1, keys=['pf_close', 'gd_close'])
df.ffill(axis=0, inplace=True)  # 填充数据
df.to_csv('pf_gd.csv')

# df = pd.read_csv('pf_gd.csv') 如果第二次运行 可以不用再次下载数据，直接读取上次保存的数据

corr = df.corr(method='pearson', min_periods=1)
print(corr)
'''
           pf_close  gd_close
pf_close   1.00000   0.69518
gd_close   0.69518   1.00000
'''
# df.plot(figsize=(20, 12))
# plt.savefig('pf_gd.jpg')
# plt.show()

# 将数值归一化
df['pf_one'] = df.pf_close / float(df.pf_close[0]) * 100
df['gd_one'] = df.gd_close / float(df.gd_close[0]) * 100

df.pf_one.plot(figsize=(20, 12))
df.gd_one.plot(figsize=(20, 12))
plt.savefig('pf_gd.jpg')
plt.close()