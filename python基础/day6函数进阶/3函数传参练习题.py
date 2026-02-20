def func(name,age,*args,**kwargs):
    print(f"我是{name}，年龄{age}，我的爱好有",end="")
    for x in args:
        print(x," ",end = "")
    print("\n我的其他信息有：")
    for k,v in kwargs.items():
        print(f"{k}：{v}")

func("张三",20,"打篮球","游泳",gender="男",nation="中国")