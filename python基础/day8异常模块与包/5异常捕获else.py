# 没有捕获异常
try:
    print(1 / 0)
except ZeroDivisionError as e:
    # 捕获到除数为0的异常时执行的代码
    print("除数不能为0",e)
else:
    # 没有异常发生时执行的代码
    print("没有异常发生")