# 捕获所有异常
try:
    open("不存在的文件.txt")
except Exception as e:
    print("捕获到异常了")
    print(e)

try:
    1 / 0
except Exception as e:
    print("捕获到异常了")
    print(e)