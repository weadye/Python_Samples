import numpy as np
import numpy.linalg as la
import time

# 计算(0,500), (1,501), (2,502), ... (499,999)这500个点之间的距离
X = np.array([range(0, 500), range(500, 1000)])
m, n = X.shape
print(m, n)  # 2 500
'''
D(i,j) = ||xi-xj||^2
'''
t = time.time()
D = np.zeros([n, n])
for i in range(n):
    for j in range(i + 1, n):
        D[i, j] = la.norm(X[:, i] - X[:, j]) ** 2
        D[j, i] = D[i, j]
print(time.time() - t)  # 1.1879029273986816
'''
|xi - xi| = sqrt((xi - xj) * (xi - xj).T)
D(i , j) = (xi - xj) * (xi - xj).T
'''
t = time.time()
D = np.zeros([n, n])
for i in range(n):
    for j in range(i + 1, n):
        d = X[:, i] - X[:, j]
        D[i, j] = np.dot(d, d)
        D[j, i] = D[i, j]
print(time.time() - t)  # 0.46709275245666504
'''
D(i , j) = (xi - xj) * (xi - xj).T
         = xi * xi.T - xi * xj.T - xj * xi.T + xj * xj.T
         = xi * xi.T - x * xi * xj.T + xj*xj.T
G(i , j) = xi.T * xj
'''
t = time.time()
G = np.dot(X.T, X)
D = np.zeros([n, n])
for i in range(n):
    for j in range(i + 1, n):
        d = X[:, i] - X[:, j]
        D[i, j] = G[i, i] - G[i, j] * 2 + G[j, j]
        D[j, i] = D[i, j]
print(time.time() - t)  # 0.4545753002166748
'''
H(i, j) = G(i, i)
K(i, j) = G(j, j) = H(i, j).T
D(i, j) = H(i, j) + K(i, j) - 2 * G(i, j)
D(i , j) = (xi - xj) * (xi - xj).T
         = xi * xi.T - xi * xj.T - xj * xi.T + xj * xj.T
         = xi * xi.T - x * xi * xj.T + xj*xj.T
G(i , j) = xi.T * xj
'''
t = time.time()
G = np.dot(X.T, X)
H = np.tile(np.diag(G), (n, 1))  # n rows, 1 for each row
D = H + H.T - G * 2
print(time.time() - t)  # 0.015627145767211914
