if int(input("请输入你的身高: ")) > 120:
    if(int(input("输入你的vip级别: ")) > 3):
        print("vip级别免费")
    else:
        print("收费10元")
else:
    print("免费")