def f02():
    print("f02 start")
    1/0
    print("f02 end")
def f01():
    print("f01 start")
    f02()
    print("f01 end")
def main():
    f01()

try:
    main()
except Exception as e:
    print("捕获到异常了")
    print(e)