age = None
for i in range(3):
    age = input("请输入年龄：")
    if age.isdigit():
        age = int(age)
        break
    else:
        print("输入有误，请重新输入！")
print(f"最后为{age}")