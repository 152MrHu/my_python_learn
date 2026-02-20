# 优化半

def my_dec(fn_name):  # 利用fn_name
    def wrapper(a, b):
        if  fn_name.__name__ == 'get_sum':
            print("开始执行加法")
        elif fn_name.__name__ == 'get_sub':
            print("开始执行减法")
        return fn_name(a, b)

    return wrapper


@my_dec
def get_sum(a,b):
    return a+b


@my_dec
def  get_sub(a,b):
    return a-b

print(get_sum(1,2))
print(get_sub(1,2))