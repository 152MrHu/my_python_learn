
"""
原函数是无参无返回的，装饰器内部函数也必须无参无返回

"""
def my_decorator(fn_name):
    def wrapper():              #有嵌套
        print("开始执行")       # 有额外功能
        fn_name()               # 有调用
        print("结束执行")
    return wrapper          # 有返回


# 原函数
@my_decorator  #对下面函数在装饰
@my_decorator
def get_sum():
    a = 10
    b = 20
    sum = a + b
    print("结果",sum)
# 传统方式
# get_sum = my_decorator(get_sum)
# get_sum()
get_sum()