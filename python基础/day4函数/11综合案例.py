
print("欢迎来到ATM。")
name = input("请输入用户名：")
money = 500000
def menu():
    """
    ATM主菜单
    :return: 用户输入的数字
    """
    print("—————————————主菜单———————————————")
    print(f"{name}你好，欢迎来到ATM。选择你的操作")
    print(f"1. 查询余额")
    print(f"2. 存款")
    print(f"3. 取款")
    print(f"4. 退出")
    return int(input("请您的选择："))
def query_money(title):
    """
    查询余额
    :return: None
    """
    if title:
        print("—————————————查询余额———————————————")
    print(f"{name}的余额为：{money}元")
def save_money():
    """
    存款
    :return: None
    """
    global money
    save_num = int(input("请输入存款金额："))
    money += save_num
    query_money(False)
def take_money():
    """
    取款
    :return: None
    """
    global money
    take_num = int(input("请输入取款金额："))
    if take_num > money:
        print("余额不足，无法取款。")
    else:
        money -= take_num
        query_money(False)

while True:
    input_num = menu()
    print(f"输入数字，{input_num}")
    if input_num == 1:
        query_money(True)
    elif input_num == 2:
        save_money()
    elif input_num == 3:
        take_money()
    elif input_num == 4:
        print("退出成功，欢迎下次使用。")
        break
    else:
        print("输入错误，请重新输入。")