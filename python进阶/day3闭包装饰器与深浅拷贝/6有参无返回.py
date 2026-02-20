

def my_decorator(fn_name):
    def wrapper(a,b):              #有嵌套
        print("开始执行")       # 有额外功能
        fn_name(a,b)               # 有调用
        print("结束执行")
    return wrapper          # 有返回


# 原函数
@my_decorator  #对下面函数在装饰
def get_sum(a,b):
    sum = a + b
    print("结果",sum)


get_sum(1,3)