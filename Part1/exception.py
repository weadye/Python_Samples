import traceback

try:
    print('try...')
    r = 10 / 0
except ZeroDivisionError as e:
    print('ZeroDivisionError', e)  # ZeroDivisionError division by zero
    print(traceback.printexc())  # 会打印出上下文
finally:
    print('finally...')
