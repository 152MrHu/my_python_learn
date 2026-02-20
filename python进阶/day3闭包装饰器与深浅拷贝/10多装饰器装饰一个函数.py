# 由内向外装饰


def check_login(fn_name):
    def wrapper():              #有嵌套
        print("校验登录")       # 有额外功能
        fn_name()               # 有调用
    return wrapper          # 有返回

def my_decorator2(fn_name):
    def wrapper():              #有嵌套
        print("开始执行2")       # 有额外功能
        fn_name()               # 有调用
    return wrapper          # 有返回

@check_login
@my_decorator2
def comment():
    print("评论")

def comment2():
    print("评论asd")

comment()
#
comment2 = my_decorator2(comment2)  # 先装饰
comment2 = check_login(comment2)        # 后装饰 先输出
comment2()