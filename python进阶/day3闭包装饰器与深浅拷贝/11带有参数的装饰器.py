


# 装饰器只能有一个参数
# 该装饰器外嵌套一层
def my_decorator(flag):   # 参数flag
    def my_dec(fn_name):
        def wrapper(a,b):
            if( flag=="+"):
                print("开始执行加法")
            elif (flag=="-"):
                print("开始执行减法")
            return fn_name(a,b)
        return wrapper
    return my_dec

@my_decorator("+")
def get_sum(a,b):
    return a+b


@my_decorator("-")
def  get_sub(a,b):
    return a-b

print(get_sum(1,2))
print(get_sub(1,2))