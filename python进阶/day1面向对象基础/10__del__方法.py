class Car:
    def __init__(self, brand, color):
        """
        :param brand:  车的品牌
        :param color:   车的颜色
        """
        print("这是init方法,创建对象自动调用")
        self.brand = brand
        self.color = color
    def __str__(self):  #print打印对象自动调用。默认是对象地址  必须有return
        return f"这是str方法,\nbrand为: {self.brand},\ncolor为: {self.color}"
    def __del__(self):
        print("这是del方法,对象被销毁自动调用")


c2 = Car([1,2,3,4,5,6], "黑色")
del c2
c1 = Car([1,2,3,4,5,6], "黑色")
print(id(c1))

print("结束")
