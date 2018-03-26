class MyClass(object):  # python默认所有的类都由object继承，所以也可以省略为 class MyClass:

    def __init__(self, val):  # 初始化函数，非构造函数
        self.val = val  # 成员变量默认都是Public类型
        self.__val = val + val  # Private类型

    def display(self, s):
        print(s, self.val)

    def displayPri(self, s):
        print(s, self.__val)


m = MyClass('abc')
print(m.val)  # abc
m.displayPri('hello')  # hello abcabc
m.display('hello')  # hello abc
print('')

m2 = m
print(id(m) == id(m2))  # true
print(id(m2))
fn = m.display
fn("hello !!!")  # hello !!! abc
