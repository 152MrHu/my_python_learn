

# 装饰器入门
"""
装饰器
"""


def check_login(fn_name):   # fn_name是被装饰的函数名 函数对象
    def fn_inner():
        #额外功能
        print("检查用户是否登录")
        fn_name()
    return fn_inner



def comment():
    print("开始执行")

"""
payment =  check_login( payment)
payment()  底层
"""
@check_login
def payment():
    print("充值中")
# 传统方式
comment()
comment =  check_login( comment)
comment()
# 新方式  语法糖
print("-"*34)
payment()
