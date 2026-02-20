

def my_decorator(fn_name):
    def wrapper(a,b):              #有嵌套
        print("开始执行")       # 有额外功能
        return fn_name(a,b)               # 有调用
    return wrapper          # 有返回


# 原函数
@my_decorator  #对下面函数在装饰
def get_sum(a,b):
    sum = b+a
    return sum

def get_sum2(a,b):
    print("AAA")
    sum = b+a
    return sum


get_sum2 = my_decorator(get_sum2)
print(get_sum2(1,2))

print(get_sum (3,4))