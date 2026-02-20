


def my_decorator(fn_name):
    def wrapper():              #有嵌套
        print("开始执行")       # 有额外功能
        return fn_name()               # 有调用
    return wrapper          # 有返回


# 原函数
@my_decorator  #对下面函数在装饰
def get_sum():
    sum = 10+20
    return sum

def get_sum2():
    return 10+50

get_sum2 = my_decorator(get_sum2)
print(get_sum2())

print(get_sum ())