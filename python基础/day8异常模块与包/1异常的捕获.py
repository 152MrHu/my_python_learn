# 异常处理 两种  停止运行与继续运行
# try except
f = None
try:
    # 可能会发生异常的代码
    f = open("C:/Users/24553/Desktop/新.txt", "r",encoding="utf-8")
except :
    # 发生异常时执行的代码
    print("文件不存在")
    f = open("C:/Users/24553/Desktop/新.txt", "w",encoding="utf-8")
# f.read()

f.close()

# x = open("C:/Users/24553/Desktop/asdwasd.txt", "r",encoding="utf-8")