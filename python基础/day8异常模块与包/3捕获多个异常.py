# 捕获多个异常 无法区分异常类型 只能知道捕获到异常了
try:
    open("不存在的文件.txt")
except (ZeroDivisionError, FileNotFoundError  )as e:
    print("捕获到异常了")

# 捕获所有异常 区分异常类型
try:
    1/0
    open("不存在的文件.txt")
except FileNotFoundError as e:
    print("捕获到异常了, 文件不存在")
    print(e)
except ZeroDivisionError as e:
    print("捕获到异常了, 除数为零")
    print(e)