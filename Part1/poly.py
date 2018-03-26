class Base:
    pass


class MyClass(Base):
    def run(self):
        print('MyClass run')


class MyClass2(Base):
    def run(self):
        print('MyClass2 run')


m = MyClass()
print(isinstance(m, MyClass))  # True
print(issubclass(MyClass2, Base))  # True
print('')

# 多态
m2 = MyClass2()
m.run()  # MyClass run
m2.run()  # MyClass2 run
print('')


def duck(d):
    d.run()


class Man:
    def run(self):
        print('man run')


class Monkey:
    def run(self):
        print('monkey run')


duck(Man())  # man run
duck(Monkey())  # monkey run
