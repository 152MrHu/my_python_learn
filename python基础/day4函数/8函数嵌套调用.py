def funca():
    print("这是函数a")

def funcb():
    print("这是函数b")
    funca()
    print("这是函数b的结束")

def funcc():
    print("这是函数c")
    funcb()
    print("这是函数c的结束")
funcc()