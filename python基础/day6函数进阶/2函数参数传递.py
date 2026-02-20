def suer_info(n,a,g):
    print(f"姓名：{n}，年龄：{a}，性别：{g}")
# 位置参数在关键值前面
suer_info("张三",20,"男")
# 关键字参数
suer_info(n="李四",a=30,g="女")
suer_info(a=30,g="女",n="李四")

# 缺损参数 默认值必须要在最右侧
def suer_info2(n,a,g="男",p="中国"):
    print(f"姓名：{n}，年龄：{a}，性别：{g} ，国籍：{p}")
suer_info2("张三",20)

# 不定长参数
def func(name,*args):   #*args 代表不定长参数，args作为一个元组传入
    print(f"组织：{name},成员有：")
    for x in args:
        print(x)
    print(type(args))
func("黑马","张三","李四","王五")

# print函数第一为*arg，后面的参数必须要使用关键字参数传入
print("-","asd","asd",end="*") # -asd*asd

# **kwargs 代表不定长关键字参数，kwargs作为一个字典传入必须用关键字参数传入
def func2(name,**kwargs):
    print(f"组织：{name},成员有：")
    for k,v in kwargs.items():
        print(f"{k}：{v}")
    print(type(kwargs))
func2("黑马",a="张三",b="李四",c="王五")

# *与**
def func3(name,*args,**kwargs):
    print(args)
    print(kwargs)
func3("黑马","张三","李四","王五",a="张三",b="李四",c="王五")
