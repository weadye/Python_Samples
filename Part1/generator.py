# 简单方法
x = range(10)
print(type(x))
sx = (x * x for x in range(10))
print(type(sx))
print(next(sx))  # 0
print(next(sx))  # 1
print(next(sx))  # 4
print(next(sx))  # 9
'''
print(next(sx))
'''
for i in sx:
    print(i)  # 16 25 36 49 64 81
print('')


# 生成器实现fib数列
def fib(limit):
    n, a, b = 0, 0, 1
    while n < limit:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

for i in fib(10):
    print(i)  # 1 1 2 3 5 8 13 21 34 55
