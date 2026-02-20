"""
nonlocal作用:

"""

def fn_outer():
    num1=100
    def fn_inner():
        nonlocal  num1
        num1 = num1 + 1
        print("结果",num1)
    return fn_inner

if __name__ == '__main__':
    fn_inner = fn_outer()
    fn_inner()
    fn_inner()
    fn_inner()