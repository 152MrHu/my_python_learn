def func(compute):
    result = compute(1, 2)
    print(result)




func(lambda x,y: x+y) # 直接传入匿名函数
func(lambda x,y:x-y) # 传入变量  变量的值是匿名函数
func(lambda x,y:x*y) # 传入变量  变量的值是匿名函数
func(lambda x,y:x/y) # 传入变量  变量的值是匿名函数

compute = lambda x,y: x//y # 匿名函数  存入变量  变量的值是匿名函数
func(compute) # 传入变量  变量的值是匿名函数