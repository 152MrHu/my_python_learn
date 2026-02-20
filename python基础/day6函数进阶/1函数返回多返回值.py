def func():
    return 1,2,3
# 自动解包
x,y,z = func()
c = func()
print(c) # (1, 2, 3)
print(x) # 1
print(y) # 2
print(z) # 3