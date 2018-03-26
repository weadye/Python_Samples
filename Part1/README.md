# Python2和3的区别
-1.在python2中，range1000000会直接生成1000000个数，用xrange则会on demand生成，而在python3中，则把两者统一了。
-2.python3中print要加括号。
-3.异常处理，python3 except ZeroDivisionError as e: |python2  except ZeroDivisionError,e:
