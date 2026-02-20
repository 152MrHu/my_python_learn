

def my_decorator(fn_name):
    def wrapper(*args,**kwargs):              #有嵌套
        print("开始执行")       # 有额外功能
        return fn_name(*args,**kwargs)               # 有调用
    return wrapper          # 有返回


# 原函数
@my_decorator  #对下面函数在装饰
def get_sum(* args,** kwargs):
    sum = 0
    for i in args:
        sum += i
    for i in kwargs.values():
        sum += i
    return sum

def get_sum2(* args,** kwargs):
    sum = 0
    for i in args:
        sum += i
    for i in kwargs.values():
        sum += i
    return sum

get_sum2 = my_decorator(get_sum2)
print(get_sum2(1,2,3,4,5,6,7,8,9,10,a=4,b=5,c=6))


su =  get_sum(1,2,3,4,5,6,7,8,9,10,a=4,b=5,c=6)
print(su)