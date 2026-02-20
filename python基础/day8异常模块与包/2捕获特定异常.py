# 捕获特定异常
"""
try:
    可能发生异常的代码
except 异常类型1 as e:
    处理异常类型1的代码
"""
try:
    1/0
except ZeroDivisionError as e:
    print("捕获到异常了, 除数为零")
    print(e)

# 捕获特定异常
try:
    open("不存在的文件.txt")
except FileNotFoundError as e:
    print("捕获到异常了, 文件不存在")
    print(e)



