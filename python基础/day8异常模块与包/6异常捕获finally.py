try:
    print(1 / 1)
except ZeroDivisionError as e:
    # 捕获到除数为0的异常时执行的代码
    print("除数不能为0",e)
except FileNotFoundError as e:
    print("捕获到异常了, 文件不存在")
    print(e)
except Exception as e:
    print("捕获到异常了")
    print(e)
else:
    # 没有异常发生时执行的代码
    print("没有异常发生")
finally:
    print("无论是否发生异常都会执行的代码")