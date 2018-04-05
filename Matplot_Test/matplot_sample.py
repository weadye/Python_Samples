import numpy as np
import matplotlib.pyplot as plt

#基本配置
plt.figure(figsize = (10,10),dpi = 80)
plt.xlim(-4.0,4.0)#坐标上下限
plt.ylim(-1.0,1.0)
'''
plt.xticks(np.linspace(-4,4,9,endpoint = True))
plt.yticks(np.linspace(-1,1,5,endpoint = True))
'''
#更直观的记号
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],['''-pi''','''-pi/2''','''0''','''pi/2''','''pi'''])
plt.yticks([-1,0,+1], ['''-1''','''0''','''+1'''])

#画曲线
X = np.linspace(-np.pi, np.pi, 256 ,endpoint= True)
Cos, Sin = np.cos(X),np.sin(X)
plt.plot(X,Cos,color = 'blue', linewidth = 1.0,linestyle='-',label = 'cos')
plt.plot(X,Sin,color = 'blue', linewidth = 1.0,linestyle='-',label = 'sin')
plt.legend(loc = 'upper left')#图例位置左上角

#移动坐标
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.show()