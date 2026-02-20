num = 10

def func():
    global num # 声明全局
    num = 100
    print("内部输出",num)
def fund():
    print(num)
fund()
func()
print(num)