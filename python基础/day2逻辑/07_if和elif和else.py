
height = int(input("请输入你的身高: "))
vip = int(input("请输入你的VIP等级: "))
day = int(input("请输入今天是几号: "))

if height < 120:
    print("你可以免票")
elif vip >= 3:
    print("你是VIP客户，可以免票")
elif day == 1:
    print("今天是1号，可以免票")
else:
    print("你需要买票")