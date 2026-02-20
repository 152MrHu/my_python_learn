"""
函数式编程：把函数当做参数传递
"""

def func(compute):
    result = compute(1,2)
    print(result)

def compute(x,y):
    return x+y

# 传入计算逻辑  不是变量和数据
func(compute)