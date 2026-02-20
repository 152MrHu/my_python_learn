age = int(input("请输入你的年龄: "))
year = int(input("请输入你的入职时间: "))
level = int(input("请输入你的级别: "))
if age>=18:
    if age<30:
        if year>=2 :
            print("入职时间满足两年，发礼物")
        elif level > 3:
            print("级别大于3发礼物")
        else:
            print("无礼物")
    else:
        print("年龄超标无礼物")
else:
    print("无礼物")