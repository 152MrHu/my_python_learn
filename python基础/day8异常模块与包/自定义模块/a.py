
def say_hi():
    print("hi")

def wangwang():
    print("a旺旺")

def add(x,y):
    return x+y

name = "张三"
age = 20
height = 1.75
print(__name__)
# 如果当前模块是主模块，__name__的值就是"__main__"
# 如果当前模块被导入了，__name__的值就是模块的名字
if __name__ == "__main__":
    wangwang()
    say_hi()
    print(add(1,2))